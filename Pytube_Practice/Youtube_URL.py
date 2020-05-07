from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def get_url(plusURL, count):
   chrome_options = webdriver.ChromeOptions()

   chrome_options.add_argument('--headless')

   chrome_options.add_argument('--no-sandbox')

   chrome_options.add_argument('--disable-dev-shm-usage')



   driver = webdriver.Chrome(r'chromedriver.exe',options = chrome_options)

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
if __name__=='__main__':
print(get_url('이영표',3))





