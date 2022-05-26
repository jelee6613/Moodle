from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Avg

import requests
import json

from pprint import pprint

from movies.serializers.quiz import QuestionSerializer

from .models import Movie, WatchedMovie, Value, Question

from .serializers.movie import MovieDetailSerializer, MovieValidationSerializer, WatchedMovieSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

User = get_user_model()

genres_dict = {
    28: '액션',
    12: '모험',
    16: '애니메이션',
    35: '코미디',
    80: '범죄',
    99: '다큐멘터리',
    18: '드라마',
    10751: '가족',
    14: '판타지',
    36: '역사',
    27: '공포',
    10402: '음악',
    9648: '미스테리',
    10749: '로맨스',
    878: 'SF',
    53: '스릴러',
    10752: '전쟁',
    37: '서부',
}

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):

    URL = 'https://api.themoviedb.org/3'  
    api_key = '04f1192a9aa395adc14e461889d716f8'
    params = {
        'api_key': api_key,
        'language': 'ko-KR',
        'region': 'KR',
    }

    GET_MOVIES_PATHS_DICT = {
        'now_playing': '/movie/now_playing',
        'upcoming': '/movie/upcoming',
        'popular': '/movie/popular',
    }

    res = {

    }

    for GET_MOVIES_PATH_NAME, GET_MOVIES_PATH in GET_MOVIES_PATHS_DICT.items():
        response_movies = requests.get(URL+GET_MOVIES_PATH, params=params)
        response_movies_json = response_movies.json()
        movies_data = response_movies_json['results']

        movies = []
        for movie_data in movies_data:

            serializer = MovieValidationSerializer(data=movie_data)
            if serializer.is_valid():
                if not Movie.objects.filter(title=movie_data['title']).exists():
                
                    # 장르 id => 한글화 작업
                    genres_datas = movie_data['genre_ids']
                    movie_genres = []
                    for genre_data in genres_datas:
                        if genres_dict[genre_data]:
                            movie_genres.append(genres_dict[genre_data])
                    
                    # list객체 JSON화 => 추후 필드에 저장 & 파싱해서 사용
                    movie_genres_json = json.dumps(movie_genres)

                    # movie의 id값으로 TMDB credits path 요청해서 감독 이름 구하기
                    GET_CREDITS_PATH = f'/movie/{movie_data["id"]}/credits'
                    response_credits = requests.get(URL+GET_CREDITS_PATH, params=params)
                    response_credits_json = response_credits.json()

                    # 영화 제작자 명단인 credits의 crew값을 변수화 => crews
                    crews_data = response_credits_json['crew']

                    # 직책이 Directing인 crew의 이름을 director 필드에 저장
                    for crew_data in crews_data:
                        if crew_data['department'] == 'Directing':
                            movie_director = crew_data['name']
                            break
                    
                    serializer.save(genre=movie_genres_json, director=movie_director)
    
                movie = get_object_or_404(Movie, title=movie_data['title'])
                serializer = MovieDetailSerializer(movie)
                movies.append(serializer.data)
        
        res[GET_MOVIES_PATH_NAME] = movies

    return Response(res)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def movie_create(request):

    URL = 'https://api.themoviedb.org/3'
    api_key = '04f1192a9aa395adc14e461889d716f8'
    keyword = request.data
    params = {
        'api_key': api_key,
        'query': keyword,
        'language': 'ko-KR',
        'region': 'KR',
    }
    
    SEARCH_MOVIES_PATH = '/search/movie'

    response_movies = requests.get(URL+SEARCH_MOVIES_PATH, params=params)
    response_movies_json = response_movies.json()
    movies_data = response_movies_json['results']

    # 전체 영화 for문 순회
    for movie_data in movies_data:

        # TMDB에서 title, overview, poster_path, release_date가 정상적인 영화만 가져옴
        serializer = MovieValidationSerializer(data=movie_data)
        if serializer.is_valid():
        
            if not Movie.objects.filter(title=movie_data['title']).exists():
                
                # 장르 id => 한글화 작업
                genres = movie_data['genre_ids']
                movie_genres = []
                for genre in genres:
                    if genres_dict[genre]:
                        movie_genres.append(genres_dict[genre])
                
                # list객체 JSON화 => 추후 필드에 저장 & 파싱해서 사용
                movie_genres_json = json.dumps(movie_genres)

                # movie의 id값으로 TMDB credits path 요청해서 감독 이름 구하기
                GET_CREDITS_PATH = f'/movie/{movie_data["id"]}/credits'
                response_credits = requests.get(URL+GET_CREDITS_PATH, params=params)
                response_credits_json = response_credits.json()

                # 영화 제작자 명단인 credits의 crew값을 변수화 => crews
                crews_data = response_credits_json['crew']

                # 직책이 Directing인 crew의 이름을 director 필드에 저장
                for crew_data in crews_data:
                    if crew_data['department'] == 'Directing':
                        movie_director = crew_data['name']
                        break

                serializer.save(genre=movie_genres_json, director=movie_director)

    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.user.id:
        if WatchedMovie.objects.filter(movie_id=movie_id, user_id=request.user.id).exists():
            watched_movie = get_object_or_404(WatchedMovie, movie_id=movie_id, user_id=request.user.id)
            serializer = WatchedMovieSerializer(watched_movie)
            return Response(serializer.data)
    
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def movie_recommendations(request):

    if request.method == 'GET':
        quizzes = Question.objects.all()
        serializer = QuestionSerializer(quizzes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # results = request.data['results']
        
        results = []
        for value_id in request.data:
            value = get_object_or_404(Value, id=value_id)
            results.append(value.director)

        recommendable_director = max(set(results), key=results.count)
        director_movies = Movie.objects.all().filter(director=recommendable_director)

        user_genres = {
            '액션': 0,
            '모험': 0,
            '애니메이션': 0,
            '코미디': 0,
            '범죄': 0,
            '다큐멘터리': 0,
            '드라마': 0,
            '가족': 0,
            '판타지': 0,
            '역사': 0,
            '공포': 0,
            '음악': 0,
            '미스테리': 0,
            '로맨스': 0,
            'SF': 0,
            '스릴러': 0,
            '전쟁': 0,
            '서부': 0,
        }

        # JSON 파싱도구
        jsonDec = json.decoder.JSONDecoder()

        movies = request.user.movies.all()

        # 사용자가 본 영화를 순회 => 각 영화의 장르를 파싱 => user_genres에 카운트
        for movie in movies:
            genres = jsonDec.decode(movie.genre)
            for genre in genres:
                user_genres[genre] += 1

        # user_genres의 value가 있는 값만(사용자가 본 장르만) 튜플 형태(장르, 카운트)로 리스트에 담고, 카운트값 기준으로 내림차순
        favorite_genres = sorted(list(filter(lambda x: x[1], user_genres.items())), key=lambda x: x[1], reverse=True)

        # 사용자가 많이 본 장르 기반으로 추천 감독의 해당 장르 영화가 있는 지 탐색 
        for favorite_genre in favorite_genres:
            if director_movies.filter(genre__contains=favorite_genre[0]).exists():
                recommendable_movie = director_movies.filter(genre__contains=favorite_genre[0]).order_by('?').first()
                break
        
        # 추천 감독의 작품 중에 사용자가 본 장르가 없다면 감독의 전체 작품 중에서 랜덤 
        else:
            recommendable_movie = director_movies.order_by('?').first()
            
        serializer = MovieDetailSerializer(recommendable_movie)
        return Response(serializer.data)


@api_view(['POST'])
def movie_rate(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    is_delete = False

    # 요청보낸 유저가 해당 영화를 본 적 있다면
    if request.user.movies.filter(pk=movie_id).exists():
        # WatchedMovie 테이블에서 요청 유저가 해당 영화를 봤다는 data 변수화
        watched_movie = get_object_or_404(WatchedMovie, movie_id=movie_id, user_id=request.user.id)

        # 평가했던 평점 그대로 재요청 보내면 내가 본 영화에서 삭제
        if not request.data['rate']:
            is_delete = True
            request.user.movies.remove(movie)

        else:
            if 5 >= request.data['rate'] >= 0.5:
                # 요청 data의 rate를 watched_movie의 rate필드에 저장/갱신
                watched_movie.rate = request.data['rate']
                watched_movie.save()
    
    else:
        if 5 >= request.data['rate'] >= 0.5:
            request.user.movies.add(movie)
            watched_movie = get_object_or_404(WatchedMovie, movie_id=movie_id, user_id=request.user.id)
            watched_movie.rate = request.data['rate']
            watched_movie.save()
    
    if WatchedMovie.objects.all().filter(movie_id=movie_id).exists():
        movie_average_vote = WatchedMovie.objects.all().filter(movie_id=movie_id).aggregate(Avg('rate'))['rate__avg']
        movie.average_vote = movie_average_vote
        movie.save()
    else:
        movie.average_vote = 0.0
        movie.save()
    
    if is_delete:
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        serializer = WatchedMovieSerializer(watched_movie)    
        return Response(serializer.data)