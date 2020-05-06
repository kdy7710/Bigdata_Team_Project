from nltk import word_tokenize


with open('stopwords',encoding='utf8') as f:
    stopwords = f.read()
    stopwords = word_tokenize(stopwords)
