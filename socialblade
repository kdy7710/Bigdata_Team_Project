from bs4 import BeautifulSoup
from selenium import webdriver
url = 'https://socialblade.com/youtube/channel/UCbFzvzDu17eDZ3RIeaLRswQ/monthly'
driver = webdriver.Chrome('chromedriver')
driver.get(url)

html = driver.page_source
driver.close()
soup = BeautifulSoup(html, 'html.parser')
test = soup.find_all('script', {'type': 'text/javascript'})
#for i, name in enumerate(test):
#    print(i,name)


import re
text = str(test[10])
start_txt = 'data:'
end_txt ='navigation'

#3번째 시작index 찾기
indice = re.finditer(start_txt,text)
indice.__next__()
indice.__next__()
start_index =indice.__next__().start()+8

#3번째 끝index 찾기
indice= re.finditer(end_txt,text)
indice.__next__()
indice.__next__()
end_index =indice.__next__().start()-19

#slice
sb_list = text[start_index: end_index].split('],[')

#값 리스트
sb_data = []
for i in sb_list[::-1]:
    sb_data.append(i.split(',')[1])
sb_data