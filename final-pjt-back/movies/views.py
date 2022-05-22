from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

import requests

from .models import Movie, WatchedMovie

from .serializers.movie import MovieDetailSerializer, MovieValidationSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

User = get_user_model()

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
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

    url = 'https://api.themoviedb.org/3'  

    path_now_playing = '/movie/now_playing'
    path_upcoming = '/movie/upcoming'
    path_popular = '/movie/popular'

    api_key = '04f1192a9aa395adc14e461889d716f8'
    params = {
        'api_key': api_key,
        'language': 'ko',
    }

    response_now_playing = requests.get(url+path_now_playing, params=params)
    now_playing_json = response_now_playing.json()
    now_playing_datas = now_playing_json['results']
    
    now_playing_movies = []
    for movie in now_playing_datas:

        # TMDB에서 title, overview, poster_path, release_date가 정상적인 영화만 가져옴
        serializer = MovieValidationSerializer(data=movie)
        if serializer.is_valid():
    
            if not Movie.objects.filter(poster_path=movie['poster_path']).exists():
                
                # 장르 id => 한글화 작업
                genres = movie['genre_ids']
                movie_genres = []
                for genre in genres:
                    if genres_dict[genre]:
                        movie_genres.append(genres_dict[genre])

                # movie의 id값으로 TMDB credits path 요청해서 감독 이름 구하기
                movie_id = movie['id']
                path_get_credits = f'/movie/{movie_id}/credits'
                response_credits = requests.get(url+path_get_credits, params=params)
                credits = response_credits.json()

                # 영화 제작자 명단인 credits의 crew값을 변수화 => crews
                crews = credits['crew']

                # 직책이 Directing인 crew의 이름을 director 필드에 저장
                for crew in crews:
                    if crew['department'] == 'Directing':
                        movie_director = crew['name']
                        break
                    
                serializer.save(genre=movie_genres, director=movie_director)
 
            now_playing_movie = get_object_or_404(Movie, poster_path=movie['poster_path'])
            serializer = MovieDetailSerializer(now_playing_movie)
            now_playing_movies.append(serializer.data)


    response_upcoming = requests.get(url+path_upcoming, params=params)
    upcoming_json = response_upcoming.json()
    upcoming_datas = upcoming_json['results']

    upcoming_movies = []
    for movie in upcoming_datas:
        
        # TMDB에서 title, overview, poster_path, release_date가 정상적인 영화만 가져옴
        serializer = MovieValidationSerializer(data=movie)
        if serializer.is_valid():
    
            if not Movie.objects.filter(poster_path=movie['poster_path']).exists():
                
                # 장르 id => 한글화 작업
                genres = movie['genre_ids']
                movie_genres = []
                for genre in genres:
                    if genres_dict[genre]:
                        movie_genres.append(genres_dict[genre])

                # movie의 id값으로 TMDB credits path 요청해서 감독 이름 구하기
                movie_id = movie['id']
                path_get_credits = f'/movie/{movie_id}/credits'
                response_credits = requests.get(url+path_get_credits, params=params)
                credits = response_credits.json()

                # 영화 제작자 명단인 credits의 crew값을 변수화 => crews
                crews = credits['crew']

                # 직책이 Directing인 crew의 이름을 director 필드에 저장
                for crew in crews:
                    if crew['department'] == 'Directing':
                        movie_director = crew['name']
                        break
                    
                serializer.save(genre=movie_genres, director=movie_director)
     
            upcoming_movie = get_object_or_404(Movie, poster_path=movie['poster_path'])
            serializer = MovieDetailSerializer(upcoming_movie)
            upcoming_movies.append(serializer.data)


    response_popular = requests.get(url+path_popular, params=params)
    popular_json = response_popular.json()
    popular_datas = popular_json['results']

    popular_movies = []
    for movie in popular_datas:
        
        # TMDB에서 title, overview, poster_path, release_date가 정상적인 영화만 가져옴
        serializer = MovieValidationSerializer(data=movie)
        if serializer.is_valid():
    
            if not Movie.objects.filter(poster_path=movie['poster_path']).exists():
                
                # 장르 id => 한글화 작업
                genres = movie['genre_ids']
                movie_genres = []
                for genre in genres:
                    if genres_dict[genre]:
                        movie_genres.append(genres_dict[genre])

                # movie의 id값으로 TMDB credits path 요청해서 감독 이름 구하기
                movie_id = movie['id']
                path_get_credits = f'/movie/{movie_id}/credits'
                response_credits = requests.get(url+path_get_credits, params=params)
                credits = response_credits.json()

                # 영화 제작자 명단인 credits의 crew값을 변수화 => crews
                crews = credits['crew']

                # 직책이 Directing인 crew의 이름을 director 필드에 저장
                for crew in crews:
                    if crew['department'] == 'Directing':
                        movie_director = crew['name']
                        break
                    
                serializer.save(genre=movie_genres, director=movie_director)
            
            popular_movie = get_object_or_404(Movie, poster_path=movie['poster_path'])
            serializer = MovieDetailSerializer(popular_movie)
            popular_movies.append(serializer.data)

    res = {
        'now_playing': now_playing_movies,
        'upcoming': upcoming_movies,
        'popular': popular_movies,
    }

    return Response(res)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def movie_create(request):

    url = 'https://api.themoviedb.org/3'
    path_get_movie_list = '/search/movie'
    api_key = '04f1192a9aa395adc14e461889d716f8'

    keyword = request.data

    params = {
        'api_key': api_key,
        'query': keyword,
        'language': 'ko'
    }

    response_movie_list = requests.get(url+path_get_movie_list, params=params)
    movie_list = response_movie_list.json()
    movies = movie_list['results']

    # 전체 영화 for문 순회
    for movie in movies:
        
        if not Movie.objects.filter(title=movie['title']).exists():

            serializer = MovieValidationSerializer(data=movie)
            if serializer.is_valid():
                
                # Movie에 넣을 영화 객체 만들기
                new_movie = Movie()
                new_movie.title = movie['title']
                new_movie.overview = movie['overview']
                new_movie.poster_path = movie['poster_path']
                new_movie.release_date = movie['release_date']

                # 장르 id => 한글화 작업
                genres = movie['genre_ids']
                movie_genres = []
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
                for genre in genres:
                    if genres_dict[genre]:
                        movie_genres.append(genres_dict[genre])

                new_movie.genre = movie_genres

                # movie의 id값으로 TMDB credits path 요청해서 감독 이름 구하기
                movie_id = movie['id']
                path_get_credits = f'/movie/{movie_id}/credits'
                response_credits = requests.get(url+path_get_credits, params=params)
                credits = response_credits.json()

                # 영화 제작자 명단인 credits의 crew값을 변수화 => crews
                crews = credits['crew']

                # 직책이 Directing인 crew의 이름을 director 필드에 저장
                for crew in crews:
                    if crew['department'] == 'Directing':
                        new_movie.director = crew['name']
                        break

                new_movie.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_recommendations(request):
    pass

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

        # 요청 data에 rate을 watched_movie의 rate필드에 저장
        if 5 >= request.data['rate'] >= 0:
            watched_movie.rate = request.data['rate']
            watched_movie.save()
    
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)