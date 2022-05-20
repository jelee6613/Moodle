from django.shortcuts import get_object_or_404
from django.http import JsonResponse

import requests

from .models import Movie

from .serializers.movie import MovieListSerializer, MovieDetailSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'POST':
        url = 'https://api.themoviedb.org/3'
        path_get_movie_list = '/movie/top_rated'
        api_key = '04f1192a9aa395adc14e461889d716f8'
        params = {
            'api_key': api_key,
            'language': 'ko-KR',
        }
        response_movie_list = requests.get(url+path_get_movie_list, params=params)
        movie_list = response_movie_list.json()
        movies = movie_list['results']

        # 전체 영화 for문 순회
        for movie in movies:
            
            if not Movie.objects.filter(title=movie['title']).exists():
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
    
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def movie_recommendations(request):
    pass

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movie_watched(request, username, movie_id):
    pass

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movie_rate(request, username, movie_id):
    pass