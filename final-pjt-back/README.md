# 영화 추천 웹사이트 PJT



## Developers

- 마주리
- 이종은



## 220517 (1일차)

1. 프로젝트 명세 작성
   - 사용자에게 어떤 서비스와 정보를 제공할 것인지를 담은 기능 요구사항을 목록화했다.
   - 사용자에게 간단한 설문을 제공해서 가치관, 성향이 비슷하거나 흥미가 가는 감독을 찾도록 유도한다. 해당 감독의 작품 중에서 사용자가 그간 평가한 영화 정보를 기반으로 새로운 영화를 추천해주는 알고리즘을 구현하기로 했다.
2. ERD 다이어그램을 이용한 모델링



## 220518 (2일차)

1. 알고리즘을 위한 quiz 모델 추가
   사용자가 감독을 찾고 나서 사용자가 그간 평가한 영화 정보를 어떻게 참고할지 고민이었다. 예를 들어 선정된 감독의 작품 중에서 사용자가 그동안 가장 많이 본 영화 장르의 작품을 추천해준다고 하면, 가장 많이 본 영화 장르를 어떻게 구현할 지 고민이었는데, 주리님의 도움으로 `group_by`를 알게 됐다.
2. URL, 컴포넌트 구상, 기록



## 220519 (3일차)

1. back
   1. 모델링
      두 모델의 id값을 갖는 M:N 테이블에 필드를 커스텀하기 위해 through 속성 이용 
      생성될 테이블을 미리 선언해서 추가하고 싶은 필드를 작성하고, ManyToManyField에 through='미리 선언한 테이블명' 속성 부여
   2. urls, views 구조 잡기
      articles, movies 앱의 urls, views 구조 잡기
2. front
   1. router 설정
      각 router마다 연결되는 view를 매칭
   2. view, components 구조 잡기
      각 view마다 하위컴포넌트 구조 잡기
   3. drf.js 작성
      프론트에서 백에 요청 보내거나 router 설정 건들 때, 쓰일 링크를 정리



## 220520 (4일차)

1. back

   1. cors & auth

      - 처음으로 client와 server 프레임워크를 구분해서 진행하는 프로젝트다. 그러기 위해서 동일 origin이 아니어도 원활한 요청과 응답이 이루어지도록 CORS 세팅을 한다. (3rd party app 설치, settings.py 수정)
      - token 정보를 기반으로 login, logout, signup 기능(urls & views)을 구현하기 위해 auth 설정을 할 수 있다. (3rd party apps 설치, settings.py 수정, 프로젝트 urls.py 포워딩)

   2. 전체 영화 조회 & 영화 추가

      - 전체 영화 목록을 Client에 출력하기 위해 Server에 GET으로 요청하면 응답하는 url & view에 POST로 요청이 들어오면 Server DB에 영화를 추가할 수 있도록 구현하고자 했다. 포스트맨으로 테스트할 땐 오픈 API에서 데이터를 잘가져왔는데 django에서 requests.get 요청하는데 유효하지 않은 key값 error, UnicodeDecode Error가 번갈아가며 나왔다.

          - 유효하지 않은 key값 : get 요청 보낼때 params로 넘겨야하는데 headers로 넘겼었다. params 인자로 넘기니 문제 해결

          - UnicodeDecode Error : requests.get 요청으로 받은 response 응답 결과는 <Response [200]> 객체일 뿐이고, .json() 메소드로 해결

            ```python
            response = requests.get(url, params=params)  # headers X, params O
                    data = response.json()
                    return Response(data)  # response X, data O
            ```

            

   3. permission

      - from rest_framework.permissions import (AllowAny, IsAdminUser....)로 각 view마다 어드민 권한자, 일반 인증회원, 비인증 회원을 구분해서 기능 구현을 할 수 있다.
        https://www.django-rest-framework.org/api-guide/permissions/

2. front

   1. pk => id
      라우터로 넘길때 라우팅인자가 계속 undefined였는데 movie.pk가 아니라 movie.id였다.



## 220521 (5일차)

back : 

1. request인자는 무조건 넣어야 할까?
   request 사용 안하는 함수는 인자에 굳이 안넣어도 될까 궁금해서 실험해봤는데 안된다. 쓰던 안쓰던 인자에 request 넣기.

2. serializers & source

   ```python
   like_users = UserSerializer(read_only=True, many=True)
   like_count = serializers.IntegerField(source='like_users.count', read_only=True)
   ```

   M:N테이블에서 article을 좋아하는 like_users의 카운트를 커스텀 필드로 생성하려면 위와 같이 IntegerField에서 source값에 스트링으로 입력하자

3. 우리 서버 DB 채우는 작업을 언제 할까?
   웹에 접속하면 첫화면에 현재상영, 개봉예정, 인기있는 영화를 Open API로 불러와서 카테고리별로 분류해서 보여준다. 사용자가 바로 영화를 선택하면 내가 본 영화 또는 평점을 남기기 위해선 우리 DB에도 있어야한다. 즉, Open API로 불러옴과 동시에 우리 DB에도 있어야 한다.

   1. 웹의 첫화면에 접속하자마자 or 첫화면에서 새로고침 할때마다 (GET요청으로 조회와 DB저장을 한번에)
      모든 사용자가 웹에 접속할때마다 또는 첫화면에서 새로고침 할때마다 Open API에서 영화 정보를 가져와서 응답해줌과 동시에 우리 DB에도 저장한다. 사용자가 웹이 버벅인다는 첫인상을 가질 수 있음과 서버에 무의미한 요청이 가지 않을까? 란 의문이 있었다.
   2. 서버 관리자가 수시로 업데이트 한다 (GET요청과 POST요청 분기)
      API 제공 웹의 DB가 변경되면 우리는 최대한 빠른 시간내에 DB 최신화 작업을 해야 한다. DB에 저장하는 요청이 필요할때만 이루어지는 점은 좋지만, 관리자가 열일해야 한다.
   3. 결론
      주리님의 의견이었던 1번으로 결정했다! 주리님과 위 방법들에 대해 이야기를 나누다가 일단 1번을 시도해보기로 했다. 약간의 버벅임이 있었지만 DB 저장 문제가 아니라 화면에 영화 정보를 보여주기 위한 Open API 요청 자체만으로 버벅인다. 우리 서비스에서 현재상영, 개봉예정, 인기있는 영화를 카테고리별로 보여주기 위해서 현재로썬 Open API 호출이 가장 효율적이므로 1번 방법이 더 나은 선택이었다.
   
4. detail 접근할 때 pk값이 아닌 title로 접근
   첫화면에 나오는 영화 정보는 TMDB 응답을 받기 때문에 detail로 넘어갈 때 pk로 안된다 => movie title로 접근



client :

1. alert 미동작
   영화를 DB에 추가하면 alert 실행코드를 넣었는데, 안됐다. => form이 submit 할때마다 prevent 설정을 해주니 해결

2. 현재 유저 정보가 새로고침 할때마다 손실
   로그인 하면 현재 유저정보의 username을 보여주는데, 새로고침 하면 사라진다. persistedstate 설치하고, user정보를 string으로 local storage에 저장한 후에 JSON으로 parsing 하니까 해결 !

   ```vue
   <template>
       ...
       <p>반갑습니다. {{ user.username }}님!</p>
   	...
   </template>
   
   <script>
   import { mapGetters } from 'vuex'
   
   export default {
     name: 'App',
     computed: {
       ...mapGetters(['currentUser']),
       user() {
         return JSON.parse(this.currentUser)
       }
     }
   }
   ```

   

## 220522 (6일차)

back :

1. from TMDB (X), DB(O) to Vue
   기존에 TMDB에서 받은 응답을 바로 Vue로 보냈다. 우리 DB에는 제목, 줄거리, 포스터경로, 개봉일이 채워져있는 영화만 저장된다. 문제점은 Vue에 보이는 영화랑 우리 DB의 영화랑 차이가 발생할 수 있다. 그래서 유효성 검사를 우선 순위에 두고, 카테고리(상영중, 개봉예정, 인기) 별로 DB에 저장되면 그 TMDB의 포스터경로 필드로 우리 DB에 같은 영화 객체를 찾고, 그 객체를 재serializing해서 카테고리별 빈리스트에 차곡차곡 append 했다.

   ```python
   		serializer.save(genre=movie_genres, director=movie_director)
   
       upcoming_movie = get_object_or_404(Movie, poster_path=movie['poster_path'])
       serializer = MovieDetailSerializer(upcoming_movie)
       upcoming_movies.append(serializer.data)
   
       ...
   
   res = {
       'now_playing': now_playing_movies,
       'upcoming': upcoming_movies,
       'popular': popular_movies,
   }
   ```

   

2. refactoring
   상영중, 개봉예정, 인기 영화를 얻어오기 위해 3번의 요청을 보낸다. 반복이므로 포문으로 코드를 한번만 작성

   ```python
   GET_MOVIES_PATHS_DICT = {
           'now_playing': '/movie/now_playing',
           'upcoming': '/movie/upcoming',
           'popular': '/movie/popular',
       }
   
       for GET_MOVIES_PATH_NAME, GET_MOVIES_PATH in GET_MOVIES_PATHS_DICT.items():
   ```



## 220523 (7일차)

1. back:

   1. dj_rest_auth의 accounts/user/ 의 serializer.data response 커스텀하기
      dj_rest_auth를 이용하면 accounts/user/ 로 요청보낼시 현재유저 정보를 admin 유저인지 확인 가능한 is_superuser 필드는 제외하고 응답받을 수 있다.
      is_superuser필드도 포함해서 받기 위해 커스텀할 수 있다. (is_superuser말고 다른 필드도 가능)

      ```python
      # settings.py
      
      REST_AUTH_SERIALIZERS = {
          'USER_DETAILS_SERIALIZER': 'accounts.serializers.user.UserSerializer',
      }
      
      # accounts/serializers/user.py
      
      # 보여주고 싶은 user필드 커스텀 시리얼라이징
      class UserSerializer(serializers.ModelSerializer):
      
          class UserFollowSerializer(serializers.ModelSerializer):
      
              class Meta:
                  model = User
                  fields = ('pk', 'username')
      
          movies = MovieDetailSerializer(many=True)
          article_set = ArticleSerializer(many=True)
          followings = UserFollowSerializer(many=True)
          followers = UserFollowSerializer(many=True)
      
          class Meta:
              model = User
              fields = ('pk', 'username', 'movies', 'followings', 'followers', 'article_set', 'is_superuser',)
      
      ```




## 220524 (8일차)

1. back:

   1. 필드에 리스트 형태를 저장하려면 ?
      sqlite에서 arrayfield는 없다. 필드에 리스트 형태로 저장해도 리스트처럼 보이는 charfield가 저장된다. ("['액션', '코미디']") 리스트를 json화 해서 필드에 저장한 후에 꺼낼땐 파싱해서 사용하면 리스트 형태로 사용할 수 있다.

      ```python
      # views.py / movies
      
      # list객체 JSON화 => 추후 필드에 저장 & 파싱해서 사용
      movie_genres_json = json.dumps(movie_genres)  # movie_genrs ['액션', '코미디']
      ...
      serializer.save(genre=movie_genres_json, director=movie_director)
      
      # JSON 파싱도구
      jsonDec = json.decoder.JSONDecoder()
      
      movies = request.user.movies.all()
      for movie in movies:
          genres = jsonDec.decode(movie.genre)
          for genre in genres:  # genrs ['액션', 코미디]
              genre # 액션
      ```

   2. 유저가 좋아하는 장르를 순위별로 표시하려면?

      1. '장르'(key): 카운트(value, integer) 형태의 딕셔너리를 만들어서 유저가 본 영화를 순회하면서 장르마다 딕셔너리의 value를 +=1 한다.

         ```python
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
         
         for movie in movies:
             genres = jsonDec.decode(movie.genre)
             for genre in genres:
                 user_genres[genre] += 1
         ```

      2. value가 0 초과한 장르만 (장르, 카운트) 튜플 형식의 객체들을 리스트화해서 카운트 기준 내림차순으로 정렬한다.

         ```python
         favorite_genres = sorted(list(filter(lambda x: x[1] > 0, user_genres.items())), key=lambda x: x[1], reverse=True)
         ```

      3. queryset에서 genre필드에 특정값이 포함된 쿼리 오브젝트들 중에서 랜덤으로 하나 뽑기

         ```python
         recommendable_movie = director_movies.filter(genre__contains=favorite_genre[0]).order_by('?').first()
         ```

      4. serializer에서 역참조 필드를 {}가 아닌 특정 필드에 바로 접근하기
         source속성을 사용해서 `source='model.field'` 로 해결

         ```python
         class ValueSerializer(serializers.ModelSerializer):
         
             question_content = serializers.CharField(source='question.content')
             class Meta:
                 model = Value
                 fields = ('__all__')
         ```

      5. loaddata & dumpdata
         loaddata 하려는데 UnicodeError 발생 !!  notepad에서 UTF-8 인코딩으로 해결



## 220525 (9일차)

1. bakc:

   1. 사용자들의 평점을 기반으로 해당 영화의 평균 평점 구하기

      ```python
      from django.db.models import Avg
      
      movie_average_vote = WatchedMovie.objects.all().filter(movie_id=movie_id).aggregate(Avg('rate'))['rate__avg']
      
      movie.average_vote = movie_average_vote
      
      
      ```

      

