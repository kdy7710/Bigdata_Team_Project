def socialblade1(url):
    """
    url = 동영상주소,
    return 값은 [[날짜,구독자수],영상업로드날짜,업로드월에 구독자수]
    """
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome('chromedriver',chrome_options=options)
    
    driver.get(url)
    elem = WebDriverWait(driver,2).until(\
        EC.presence_of_element_located((By.CSS_SELECTOR, \
        '#date > yt-formatted-string')))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select('#date > yt-formatted-string')
    upload_date = notices[0].text #동영상 올린날짜 string
    upload_date = upload_date.replace('. ','-').replace('.','')
    import datetime
    upload_date = datetime.datetime.strptime(upload_date,"%Y-%m-%d")
    upload_date = str(upload_date)[:10]
    driver.find_element_by_css_selector('ytd-channel-name.ytd-video-owner-renderer > div > div > yt-formatted-string> a').click()
    elem = WebDriverWait(driver,2).until(\
        EC.presence_of_element_located((By.CSS_SELECTOR, \
        '#text')))
    channel_url = driver.current_url #채널url획득
  
      
    """channerurl는 영상url 
       출력값은 2차원리스트로 [날짜, 구독자] 
    """
    youtube_id = channel_url.split('/')[-1]

    #소셜블레이드에 해당유튜버의 detailed statistics 페이지에 들어가서 크롤링
    social_url = 'https://socialblade.com/youtube/channel/'+youtube_id+'/monthly'
    driver.get(social_url)
    elem = WebDriverWait(driver,2).until(\
        EC.presence_of_element_located((By.CSS_SELECTOR, \
        '#socialblade-user-content > div> div')))
    
    html = driver.page_source
    driver.close()
    text = str(BeautifulSoup(html, 'html.parser'))
    
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
    
    for i in sb_data[::-1]:
        if (i[0]<upload_date):
            result = i
            break
            
            

 
    return [sb_data,upload_date,result]

if __name__=='__main__':
    url='https://www.youtube.com/watch?v=S2fDoILcLDQ'
    for i in socialblade1(url):
        print(i)