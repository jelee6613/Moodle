# MOODLE, 당신만의 영화 감독을 찾아보세요!

- 삼성 청년 SW아카데미 관통프로젝트 최우수상🏆
- 2022년 5월 17일 ~ 2022년 5월 26일


![MOODLE.png](assets/메인.png)

<span>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=Django&logoColor=white">
<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</span>
<br>
<span>
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white">
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
</span>
<br>
<span>
<img src="https://img.shields.io/badge/GitLab-FCA121?style=for-the-badge&logo=GitLab&logoColor=white">
<img src="https://img.shields.io/badge/Mattermost-0058CC?style=for-the-badge&logo=Mattermost&logoColor=white">
<img src="https://img.shields.io/badge/visual studio code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
</span>

<br>

## 목차

1️⃣ <a href="#1️⃣-개요">개요</a>

2️⃣ <a href="#2️⃣-기여도">기여도</a>

3️⃣ <a href="#3️⃣-설계">설계</a>

4️⃣ <a href="#4️⃣-시연">시연</a>

5️⃣ <a href="#5️⃣-개발자">개발자</a>

6️⃣ <a href="#6️⃣-회고">회고</a>


<br>

## 1️⃣ 개요

- TMDB API를 이용해 영화 정보를 불러와 영화 데이터를 사용자에게 보여주고 추천도 해줘요!
- 간단한 퀴즈를 읽고 해당하는 보기를 고르면 당신과 비슷한 성향의 감독을 찾아드립니다!
- 나와 가장 닮은 감독의 영화 중 내 취향에 딱 맞는 영화를 추천해드려요!
- 추천 받은 영화를 감상하면 커뮤니티에서 다른 사람과 함께 영화에 대한 이야기를 나눠보세요~

<br>

## 2️⃣ 기여도

### 🔸 Backend

<span>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Django-000000?style=for-the-badge&logo=Django&logoColor=white">
<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
</span>

<br>

<span>
<img src="https://img.shields.io/badge/GitLab-FCA121?style=for-the-badge&logo=GitLab&logoColor=white">
<img src="https://img.shields.io/badge/Mattermost-0058CC?style=for-the-badge&logo=Mattermost&logoColor=white">
<img src="https://img.shields.io/badge/visual studio code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
</span>

> 영화 추천 아이디어 기획과 구현을 포함한 Backend 업무를 수행했습니다.  
> 사용자가 간단한 설문을 진행하면 비슷한 성향의 영화 감독을 찾아내고, 해당 영화 감독의 작품 중에서 사용자가 관람한 영화 데이터를 분석해서 선호하는 장르의 작품을 추천하는 알고리즘을 구현했습니다.

#### ◼ 기획

◽ 영화 추천 

#### ◼ 설계

◽ ERD 작성

◽ Components 설계

◽ Routes 설계

#### ◼ 개발

◽ REST API 구축

◽ Open API 활용

◽ RDBMS 관리

◽ 영화 추천 알고리즘

<br>

## 3️⃣ 설계

### 🔸 ERD

![erd](assets/erd.png)

### 🔸 Components & Routes 구조

![front](assets/front.png)

<br>

## 4️⃣ 시연

### 👇Click!

[![시연영상](assets/로고.png)](https://youtu.be/ALXX5F6ty6w) 

0:00 - 메인페이지 & 상세페이지

0:18 - 로그인

0:25 - 영화 평점 기능

0:44 - 프로필 화면

0:56 - 회원가입

1:08 - 사용자들의 평균 평점 제공

1:26 - 커뮤니티 기능

2:13 - 팔로우 기능

2:17 - 영화 추천 서비스 기능

<br>

## 5️⃣ 개발자

| 이름 | 역할 |
| --- | --- |
| 👩마주리 | Frontend |
| 👨이종은 (me) | Backend |

<br>

## 6️⃣ 회고

### 🔸 핵심기능

<details>
<summary>TMDB API 데이터 가공</summary>
  
TMDB API는 영화의 장르 정보를 `Integer`가 담긴 `List`로 제공하고 있다. 사용자에게 `Integer`가 아닌 한글로 장르 정보를 제공하고자 아래와 같이 `Integer(Key)` : `String(Value)` 구조의 `genres_dict(Dictionary)`를 만들어 활용했다.
  
```python
genres_dict = {
    28: '액션',
    12: '모험',
    16: '애니메이션',
    35: '코미디',
    80: '범죄',
    ...(이하 생략)...
}
``` 

<br>

영화 출연진과 제작진을 응답으로 주는 Path로 요청을 보내 영화 감독 이름을 구하고, 이를 `movie_director`에 할당한다. 마지막에 genre와 director에 값을 넣고, save!

```python
# movie의 id값으로 TMDB credits path 요청해서 감독 이름 구하기
GET_CREDITS_PATH = f'/movie/{movie_data["id"]}/credits'
response_credits = requests.get(URL+GET_CREDITS_PATH, params=params)
response_credits_json = response_credits.json()

# 영화 제작자 명단인 credits의 속성 crew의 값을 변수화 => crews_data
crews_data = response_credits_json['crew']

# 직책이 Directing인 crew의 이름을 director 필드에 저장
for crew_data in crews_data:
    if crew_data['department'] == 'Directing':
        movie_director = crew_data['name']
        break

serializer.save(genre=movie_genres_json, director=movie_director)
```
</details>

<details>
<summary>사용자와 비슷한 성향의 영화 감독 찾기</summary>
  
사용자가 제출한 설문 결과인 `request.data`를 순회하면 `Integer` 객체에 접근할 수 있다. 이를 `Value` 모델의 `value_id`로 조회하면 해당하는 감독 이름을 찾을 수 있다. 가장 많이 선택된 감독을 찾고, 그 감독의 모든 영화(`director_movies`)를 찾는다.

```python
results = []
for value_id in request.data:
    value = get_object_or_404(Value, id=value_id)
    results.append(value.director)

recommendable_director = max(set(results), key=results.count)
director_movies = Movie.objects.all().filter(director=recommendable_director)
```
    
</details>

<details>
<summary>사용자가 많이 본 장르 찾기</summary>
  
사용자가 관람한 영화를 순회하며 관람한 장르를 횟수로 집계하고, 내림차순 정렬한다. 이는 객체 `favorite_genres`에 해당한다. `favorite_genres`를 순회하면 사용자가 가장 많이 본 장르가 순서대로 나오며, 영화 감독 작품 중에 일치하는 장르가 있으면 `recommendable_movie`에 할당하고, 이를 반환한다. 만약 반복문이 끝날 때까지 일치하는 장르가 없으면 감독의 영화 중 무작위로 하나의 영화를 반환한다.

```python
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
```
    
</details>

<br>

### 🔸 문제해결

<details>
<summary>SQLite3 리스트 필드 저장하기</summary>

SQLite3는 `List` 객체를 저장할 수 없다. 그렇지만 `List`를 `JSON`으로 만들어서 저장하고,  꺼낼 땐 파싱하면 사용할 수 있다.

```python
# list객체를 JSON으로 변환해서 저장하고, 꺼낼 땐 파싱해서 사용한다.
movie_genres_json = json.dumps(movie_genres)
```
    
</details>

<details>
<summary>한 번의 작업으로 TMDB API에 3 번의 요청을 보내고, DB에 저장한 뒤에 요청을 구분해서 한 번에 응답하기</summary>
  
Path별로 반복문을 돌리면서 TMDB API에 요청을 보낸다. DB에 데이터를 저장하고, 저장이 끝나면 DB에서 해당 영화가 가진 유일한 속성-값으로 다시 찾아낸 다음 빈 `movies(List)`에 채운다. 각 Path 요청으로 채워진 `movies(List)`는 마지막 응답으로 보낼 `res(Dictionary)`에 Path 이름을 Key값으로 가지는 Value로 할당한다.
    
```python
GET_MOVIES_PATHS_DICT = {
    'now_playing': '/movie/now_playing',
    'upcoming': '/movie/upcoming',
    'popular': '/movie/popular',
}

res = {}

for GET_MOVIES_PATH_NAME, GET_MOVIES_PATH in GET_MOVIES_PATHS_DICT.items():
    response_movies = requests.get(URL+GET_MOVIES_PATH, params=params)
    response_movies_json = response_movies.json()
    movies_data = response_movies_json['results']

    movies = []
    # TMDB API에서 응답으로 받은 영화를 하나씩 순회
    for movie_data in movies_data:
          ...
                # DB에 저장!
                serializer.save(genre=movie_genres_json, director=movie_director)
            
            # DB에 저장하자마자 movies에 담는다.
            movie = get_object_or_404(Movie, title=movie_data['title'])
            serializer = MovieDetailSerializer(movie)
            movies.append(serializer.data)
            
    # 최종 응답으로 보낼 딕셔너리에 해당하는 Path 값의 Value로 movies를 할당한다.
    res[GET_MOVIES_PATH_NAME] = movies

return Response(res)
```
    
</details>

<br>

### 🔸 아쉬운점

<details>
<summary>커뮤니티 이미지 업로드 기능</summary>
커뮤니티에 게시글을 올릴 때 오직 글만 올라갈 수 있어서 이미지도 추가해서 좀 더 다양한 정보들이 오갈 수 있도록 개선하면 좋을 것 같다.
</details>

<details>
<summary>맞팔로우 방명록 기능</summary>
여론조사에 따르면 사람들은 주변 지인, SNS에서 영화를 추천 받는 경우가 많았다. 서로의 프로필 페이지에 방명록 기능을 추가하면 사용자끼리 보다 적극적인 영화 추천이 이루어질 것 같다.
</details>

<a href="#moodle-당신만의-영화-감독을-찾아보세요">⏏맨 위로</a>
