import nltk
from matplotlib import font_manager, rc
from nltk.tokenize import TweetTokenizer

with open('test.txt','r') as f:
    content = f.read()


    tokenizer = TweetTokenizer() # 단어별로 토크나이징
    tk = tokenizer.tokenize(content) # 토크나이징 된 리스트인 content Text객체에 넣어줌
    ko = nltk.Text(tk)

    # 분석기 쓰려면 자바 설치 해야함
    from konlpy.tag import Komoran

    km = Komoran()
    print(km.nouns(content))


    ### 한국어 설정
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

    ko.plot(50)

    print(ko.count('너무'))

    print(type(tk))
    print(ko.vocab())

    ko.plot(20) # t