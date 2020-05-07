def get_channelurl(url):
    """
    url = 동영상주소,
    return 값은 채널 주소
    """
    from bs4 import BeautifulSoup
    from selenium import webdriver
    driver = webdriver.Chrome('chromedriver')
    driver.get(url)
    driver.find_element_by_css_selector('ytd-channel-name.ytd-video-owner-renderer > div:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(1) > a:nth-child(1)').click()
    'yt-formatted-string.ytd-video-primary-info-renderer:nth-child(2)'
    channel_url = driver.current_url
    driver.close()
    return channel_url

#테스트용코드 import로 다른 파일에서 실행시에는 실행되지 않음
if __name__=='__main__':
    url='https://www.youtube.com/watch?v=zi62bIm6jCw'
    print(get_channelurl(url))