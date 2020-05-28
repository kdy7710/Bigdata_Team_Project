# Team_Project

### 프로젝트 아이디어
#### 1번안 
* 구독자 높은 vs 구독자 적은
영상 크롤링후
키워드 네이버, 구글에 검색트랜드 변화확인
<뷰티 인플루언서>  

keywords = glowpick keywords 추출 (약 80000개)


Youtube_URL.search(keywords) --> return url(상위 3 개 ..70000*3)
*채널명
*저장 루틴만들기!!

socialblade2.socialblade1(url)

 """
    url = 동영상주소,
    return 값은 [[날짜,구독자수],영상업로드날짜,업로드월에 구독자수]
 """

Naver_Api.API_CLASS.NaverApi(keyword, 영상업로드날짜)

--> 날짜별 검색율 df 

날짜별 검색율 df ,업로드월에 구독자수



분석

구독자 수 그룹핑 

검색율 점수 매김
avg(영상 올린날, +1,+2)/(영상올리기전날)


#### 2번안
* 네이버나 구글에서 키워드 획득후
유튜브에 키워드 검색
검색된 영상의 업로드 날짜, 구독자 수 확인
네이버 구글 트랜드 비교

#### 3번안
* 드라마 ppl 효과 분석
* 데이터 링크: https://www.datastore.or.kr/api/detail?id=9c126310-5db9-4698-8a60-c9937963b14b
* 프로그램 속성 파악 (시청률, 시간대, 시청자 군, 방송사)

#### 4번안 
* 지역별 택배량과 전기량의 상관관계
* 가설: 택배량과 전기량은 서로 비례할 것이다
* 쿠팡 Api 사용 
* 전기량 정보 수집 

### 주의사항 
 
* Wordcloud
  wordcloud 파라미터(옵션) 중
  font_path 지정이 잘못될 경우 오류 발생(명확한 오류메시지가 안나옴)
  같은 work space에 위치시켜
  font_path='폰트명.확장자'로 쓰거나
  절대경로로 지정을 해줘야함.

ex)
...
wordcloud = WordCloud(font_path='../SDKukdetopokki-aLt.otf',
                       width=2400, height=1800,
                       ranks_only=True
...
 
* test1234
다른 계정으로 접속

 
 * subscriber_stat\socialblade.py 등
  selenium 혹은 webdriver 사용시
  selenium 설치(pip install selenium) 선행 되어야함.

 
* webdriver 사용 시(chrome driver 등)
브라우저의 버전과 드라이버의 버전을 잘 맞춰주어야함.
