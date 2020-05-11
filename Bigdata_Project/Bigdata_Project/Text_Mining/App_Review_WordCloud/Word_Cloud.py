from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
from AppReview_Wordcloud.CsvRead import content # 앱 리뷰 string 뭉텅이
from analyze import text
from nltk.sentiment.vader import SentimentIntensityAnalyzer # 감정분석
from nltk import tokenize # 문장별로 쪼갬
import nltk

word = tokenize.word_tokenize(text) # 단어별로 tokenize
ko = nltk.Text(word) # text




print(ko.tokens) # 단어별로 나눈거 리스트로 리턴
data = ko.vocab().items()

print(data) # 단어와 단어빈도수 딕셔너리로 리턴
print(type(data))



############감정분석#############
sid = SentimentIntensityAnalyzer()

# content 뭉텅이를 문장별로 리스트에 담아 리턴
lines_list = tokenize.sent_tokenize(content)
for sent in lines_list:
    # ss 는 한문장에 대한 neg, neu, pos, compound 정도를 딕셔너리 형식으로 가지고 있음
    ss = sid.polarity_scores(sent)







############### 워드클라우드 #####################

# Generate a word cloud image
wordcloud = WordCloud(font_path='../SDKukdetopokki-aLt.otf',
                      width=2400, height=1800,
                      ranks_only=True,  # 빈도수가 아닌 단어빈도수 순위로 글자 크기 결정
                      relative_scaling = 0.0,  #단어 등장 빈도에 따른 크기 차이를 조절하는 비율값
                      stopwords = set(STOPWORDS)  # STOPWORDS는 의미없는 단어들을 모아놓은 wordcloud 내장 리스트
                      ).generate(content)

# Display the generated image:
# the matplotlib way:
fig = plt.figure()
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

plt.plot(10)
os.makedirs('C:/Users/TT_L/Desktop/WordCloud_ex',exist_ok=True)

# 워드클라우드 사진 저장
plt.savefig('C:/Users/TT_L/Desktop/WordCloud_ex/Google_App_Review_1.png')
