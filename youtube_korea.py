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
    for i in embedlist:
        html = requests.get(i).text
        soup = BeautifulSoup(html,'html.parser')
        if soup.find('link',{'rel':"canonical"} ) == None:
            continue
        a =soup.find('link',{'rel':"canonical"} )['href']
        video_url.append(a)
    return video_url