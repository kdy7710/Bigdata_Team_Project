# import requests
# from bs4 import BeautifulSoup
# url = 'https://www.youtube.com/watch?v=zi62bIm6jCw'
# html = requests.get(url).text
# soup = BeautifulSoup(html,'html.parser')

def check_url(soup):
    if soup.find('span',{'class':'yt-uix-button-content'})==None:
        return 0
    else:
        return -1
    
# check_url(soup)