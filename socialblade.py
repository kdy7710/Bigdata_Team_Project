def socialblade(youtube_id):
    """youtube_id는 유튜브url https://www.youtube.com/channel/ 혹은 https://www.youtube.com/user/ 뒤에 붙어 있는 아이디 혹은 문자열, 
       출력값은 2차원리스트로 날짜, 구독자 순
    """
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
    sub_txt='graph-youtube-monthly-subscribers-container'
    start_txt = 'data:'
    end_txt ='navigation'
    
    text = text[text.index(sub_txt):]
    text = text[text.index(start_txt)+8:text.index(end_txt)-19]
    
#     #시작index 찾기
#     indice = re.finditer(start_txt,text)
#     for i in range(chart_no-1):
#         indice.__next__()
#     start_index =indice.__next__().start()+8

#     #끝index 찾기
#     indice= re.finditer(end_txt,text)
#     for i in range(chart_no-1):
#         indice.__next__()
#     end_index =indice.__next__().start()-19

    #slice
    sb_list = text.split('],[')

#     #값 리스트 생성
    sb_data = []
#    if chart_no in (3,4,5,6):
    for i in sb_list[::-1]:
        sb_data.append(i.split(',')[1])
#     else: #1,2는 배열뒤집을 필요없음
#         for i in sb_list:
#             sb_data.append(i.split(',')[1])
#     #return sb_data
    
    #날짜 생성 준비
    import datetime
    today = datetime.datetime.today()
    date =[]
    
#     #데이터 따라서 적합한 날짜 간격생성
        
#     if chart_no in (3,4):
    timeframe=30
    for i in range(len(sb_data)):
        today = today - datetime.timedelta(days=timeframe)
        date.append(str(today)[:10])
#     elif chart_no in (5,6):
#         timeframe=8
#         for i in range(len(sb_data)):
#             date.append(str(today)[:10])
#             today = today - datetime.timedelta(days=timeframe)
#     else: #1,2일때
#         timeframe=7
#         for i in range(len(sb_data)):
#             date.append(str(today)[:10])
#             today = today - datetime.timedelta(days=timeframe)        
            
    #날짜 데이터 합치기    
    return(list(zip(reversed(date),sb_data)))

if __name__=='__main__':
    a = socialblade('UC78PMQprrZTbU0IlMDsYZPw')
    print(a)