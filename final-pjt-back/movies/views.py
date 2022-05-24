from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

import requests
import json

from .models import Movie, WatchedMovie

from .serializers.movie import MovieDetailSerializer, MovieValidationSerializer

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
        'language': 'ko',
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
                if not Movie.objects.filter(poster_path=movie_data['poster_path']).exists():
                
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
    
                movie = get_object_or_404(Movie, poster_path=movie_data['poster_path'])
                serializer = MovieDetailSerializer(movie)
                movies.append(serializer.data)
        
        res[GET_MOVIES_PATH_NAME] = movies

    return Response(res)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def movie_create(request):

    URL = 'https://api.themoviedb.org/3'
    api_key = '04f1192a9aa395adc14e461889d716f8'
    params = {
        'api_key': api_key,
        'query': keyword,
        'language': 'ko'
    }
    keyword = request.data
    
    SEARCH_MOVIES_PATH = '/search/movie'

    response_movies = requests.get(URL+SEARCH_MOVIES_PATH, params=params)
    response_movies_json = response_movies.json()
    movies_data = response_movies_json['results']

    # 전체 영화 for문 순회
    for movie_data in movies_data:

        # TMDB에서 title, overview, poster_path, release_date가 정상적인 영화만 가져옴
        serializer = MovieValidationSerializer(data=movie_data)
        if serializer.is_valid():
        
            if not Movie.objects.filter(poster_path=movie_data['poster_path']).exists():
                
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
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_recommendations(request):
    results = request.data['results']
    recommendable_director = max(set(results), key=results.count)

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

    for movie in movies:
        genres = jsonDec.decode(movie.genre)
        for genre in genres:
            user_genres[genre] += 1

    favorite_genres = list(filter(lambda x: x[1] > 0, user_genres.items()))
    favorite_genres = sorted(favorite_genres, key=lambda x: x[1], reverse=True)
    
    for favorite_genre in favorite_genres:
        director_movies = Movie.objects.all().filter(director=recommendable_director)
        print(director_movies)
    return Response()


## 삭제 예정
@api_view(['POST'])
def movie_watched(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # 내가 본 영화 등록/취소
    if request.user.movies.filter(pk=movie_id).exists():
        request.user.movies.remove(movie)
    else:
        request.user.movies.add(movie)
    
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def movie_rate(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    # 요청보낸 유저가 해당 영화를 본 적 있다면
    if request.user.movies.filter(pk=movie_id).exists():
        # WatchedMovie 테이블에서 요청 유저가 해당 영화를 봤다는 data 변수화
        watched_movie = get_object_or_404(WatchedMovie, movie_id=movie_id, user_id=request.user.id)

        # 평가했던 평점 그대로 재요청 보내면 내가 본 영화에서 삭제
        if request.data['rate'] == watched_movie.rate:
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

    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)