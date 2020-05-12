# Team_Project
### 여기에 프로젝트 설명 추가 

### 프로젝트 아이디어
#### 1번안 
* 구독자 높은 vs 구독자 적은
영상 크롤링후
키워드 네이버, 구글에 검색트랜드 변화확인

#### 2번안
* 네이버나 구글에서 키워드 획득후
유튜브에 키워드 검색
검색된 영상의 업로드 날짜, 구독자 수 확인
네이버 구글 트랜드 비교
#### 3번안
* 드라마 ppl 데이터 수집 가능 여부 파악

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
