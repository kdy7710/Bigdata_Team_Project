<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup

def search(keyword):
   """
   * 특정 키워드로 검색했을 때 영상 url과 제목을 요소로 가진 2차원 리스트로 리턴 
   
   -----Example----
   호출 : search('화장품')
   함수리턴값:
   [['https://www.youtube.com/results?search_query=/channel/UCqrNqg3UgVoD3Sa-F_TxuSA', '디렉터 파이'], ['https://www.youtube.com/results?search_query=/watch?v=6Jo9SsJ5bhc', '(*Eng) 여드름, 블랙헤드 고민러 모여라! 패드 효과 제대로 보 
   는 법 따로 있다?!! by 디렉터파이'], ['https://www.youtube.com/results?search_query=/watch?v=It_9NCkKhkY', '[ENG] 처음이쥬? 디파네 연구소장님과 화장품 성분 딥하게 파기 by 디렉터파이']]
   
   """
   result = []
    
   baseurl = 'https://www.youtube.com/results?search_query='
   plusurl = keyword
   url = baseurl + plusurl
    
   html = requests.get(url).content
   soup = BeautifulSoup(html, 'html.parser')
   
   videos = soup.find_all('a', class_ = 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ')
   count = 0
   for i in videos:
      content=[]
      if count >= 3: # 상위 3개만 
         break
      elif i.attrs['title'] :
         title = i.attrs['title']
         href = baseurl + i.attrs['href']
         content.append(href)
         content.append(title)
         result.append(content)
          
         count +=1
   return result 


if __name__ == "__main__":
   # import pandas as pd
   # dic = {}
   # df = pd.read_excel('C:/Users/tjoeun/Documents/GitHub/Team_Projects/Bigdata_Project/Bigdata_Project/Pytube_Practice/brand_name.xlsx')
   # for item in df['상품명']:
   #    dic[item] = search(item)


   # pd.DataFrame(dic)
   # print(pd)
   print(search('화장품'))

=======
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_url(plusURL, count):
   chrome_options = webdriver.ChromeOptions()

   chrome_options.add_argument('--headless')

   chrome_options.add_argument('--no-sandbox')

   chrome_options.add_argument('--disable-dev-shm-usage')



   driver = webdriver.Chrome('chromedriver.exe', options = chrome_options)

   baseURL = 'https://www.youtube.com/results?search_query='



   URL = baseURL + plusURL

   driver.get(URL)


   # 스크롤
   body = driver.find_element_by_css_selector('body')

   while True:
      body.send_keys(Keys.PAGE_DOWN)
      time.sleep(0.5)
      body.send_keys(Keys.PAGE_DOWN)
      time.sleep(0.5)

      html = driver.page_source
      soup = BeautifulSoup(html, 'html.parser')
      videos = soup.find_all('a', class_='yt-simple-endpoint style-scope ytd-video-renderer')

      if len(videos) >= int(count):
         break


   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')
   videos = soup.find_all('a', class_ = 'yt-simple-endpoint style-scope ytd-video-renderer' )

   videolist = []
   baseURL = 'https://www.youtube.com'


   for i in range(0,int(count)):
      href = videos[i].attrs['href']
      vidurl = baseURL+href
      videolist.append(vidurl)



   return(videolist)
>>>>>>> 4b8a4ee448207283a7d76cea824aaf619d991bcc

 


<<<<<<< HEAD
=======



>>>>>>> 4b8a4ee448207283a7d76cea824aaf619d991bcc
