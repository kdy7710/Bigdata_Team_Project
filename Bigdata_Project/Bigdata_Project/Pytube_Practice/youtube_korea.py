def youtube_korea():
    import requests
    from bs4 import BeautifulSoup
    embedlist =[]
    for j in range(1,20):
        url = 'http://www.youtubemarketing.co.kr/brandVideo/'+str(j)
        html = requests.get(url).text
        soup = BeautifulSoup(html,'html.parser')
        a = soup.find_all('a', {'class':'link_brand'})
        for i in a:
            i = str(i)
            if i.find('https://www.youtube.com/embed')== -1:
                continue
            i = i[i.index('http'):]
            if i.find(',')== -1:
                continue
            i=i[:i.index(',')-1]
            embedlist.append(i)   
    embedlist
    video_url =[]
    url_prefix = 'https://www.youtube.com/watch?v='
    for i in range(len(embedlist)):
        video_url.append(url_prefix+embedlist[i].split('/')[-1])   
    return video_url

if __name__=='__main__':
    video_url()