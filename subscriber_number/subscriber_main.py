def subscriber_main(url):
    """
    url = 동영상url,
    get_channelurl.py랑 socialblade.py연결해서 구독자수추이 출력
    """
    import socialblade
    import get_channelurl
    a=get_channelurl.get_channelurl(url)
    return socialblade.socialblade(a)
    
#테스트용코드 import로 다른 파일에서 실행시에는 실행되지 않음
if __name__=='__main__':
    url='https://www.youtube.com/watch?v=zi62bIm6jCw'
    print(subscriber_main(url) )