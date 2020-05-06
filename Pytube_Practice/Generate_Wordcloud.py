from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from analyze import text
from stopwords import stopwords
import nltk



with open('test.txt', 'w') as f :
    f.write(text)


############### 워드클라우드 #####################
#
# # Generate a word cloud image
# wordcloud = WordCloud(font_path='../SDKukdetopokki-aLt.otf',
#                       width=2400, height=1800,
#                       ranks_only=True,  # 빈도수가 아닌 단어빈도수 순위로 글자 크기 결정
#                       relative_scaling = 0.0,  # 단어 등장 빈도에 따른 크기 차이를 조절하는 비율값
#                       stopwords = set(stopwords)  # STOPWORDS는 의미없는 단어들을 모아놓은 wordcloud 내장 리스트
#                       ).generate(text)
#
# # Display the generated image:
# # the matplotlib way:
# fig = plt.figure()
# plt.imshow(wordcloud)
# plt.axis('off')
#
#
#
# ko =nltk.Text(text)
# print(ko.vocab())
# print(ko.plot(20))
#
# plt.show()
# os.makedirs('C:/Users/TT_L/Desktop/WordCloud_ex',exist_ok=True)
#
# # 워드클라우드 사진 저장
# plt.savefig('C:/Users/TT_L/Desktop/WordCloud_ex/Son.png')
