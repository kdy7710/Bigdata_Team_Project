def socialblade(youtube_id, chart_no):
    """youtube_id는 유튜브url https://www.youtube.com/channel/ 뒤에 붙어 있는 아이디, 
       chart_no는 socialblade에 detailed statistics에 있는 javascript상에 차트 순번,
       출력값은 리스트로 차트 결과값
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
    
    #for i, name in enumerate(test):
    #    print(i,name)

    #javascript내에 있는 데이터 위치 찾기(10번째)
    import re
    text = str(test[10])
    start_txt = 'data:'
    end_txt ='navigation'

    #3번째 시작index 찾기
    indice = re.finditer(start_txt,text)
    for i in range(chart_no-1):
        indice.__next__()
    start_index =indice.__next__().start()+8

    #3번째 끝index 찾기
    indice= re.finditer(end_txt,text)
    for i in range(chart_no-1):
        indice.__next__()
    end_index =indice.__next__().start()-19

    #slice
    sb_list = text[start_index: end_index].split('],[')

    #값 리스트
    sb_data = []
    for i in sb_list[::-1]:
        sb_data.append(i.split(',')[1])
    return sb_data


#테스트용 코드 (단독실행 일때만 실행되고 다른곳에서 import하면 실행안됨)
if __name__=='__main__':
    a = socialblade('UCbFzvzDu17eDZ3RIeaLRswQ',5)
    print(a)