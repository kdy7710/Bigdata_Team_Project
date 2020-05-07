def socialblade(channelurl):
    """channerurl는 영상url 
       출력값은 2차원리스트로 [날짜, 구독자] 
    """
    youtube_id = channelurl.split('/')[-1]

    from bs4 import BeautifulSoup
    from selenium import webdriver

    #소셜블레이드에 해당유튜버의 detailed statistics 페이지에 들어가서 크롤링
    url = 'https://socialblade.com/youtube/channel/'+youtube_id+'/monthly'
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    html = driver.page_source
    driver.close()


    soup = BeautifulSoup(html, 'html.parser')
    test = soup.find_all('script', {'type': 'text/javascript'})
    
    #javascript내에 있는 데이터 위치 찾기(10번째)
    import re
    text = str(test[10])

    #데이터 위치 인덱스 찾아서 데이터를 리스트로 변환
    sub_txt='graph-youtube-monthly-subscribers-container'
    start_txt = 'data:'
    end_txt ='navigation'
    text = text[text.index(sub_txt):]
    text = text[text.index(start_txt)+8:text.index(end_txt)-19]
    sb_list = text.split('],[')

    #유닉스타임 시간변환 함수만들기
    def convert(time):
        import datetime
        date = datetime.datetime.fromtimestamp(time/1000).strftime('%Y-%m-%d')
        return date
    
    #값 리스트 생성
    sb_data = []
    for i in sb_list[::-1]:
        a=convert(int(i.split(',')[0])) #시간함수적용
        b=i.split(',')[1]
        li=[a,b]
        sb_data.append(li)
          
    return(sb_data)

#테스트용코드 import로 다른 파일에서 실행시에는 실행되지 않음
if __name__=='__main__':
    a = socialblade('https://www.youtube.com/channel/UCk6bX-MZXdte_7kG8TbMkqg')
    print(a)