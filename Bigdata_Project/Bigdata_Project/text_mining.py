def get_stopwords():
    from nltk import word_tokenize


    with open('stopwords',encoding='utf8') as f:
        stopwords = f.read()
        stopwords = word_tokenize(stopwords)
    return(stopwords)
   
def get_nouns(file_path):
    from konlpy.tag import Kkma
    km = Kkma()
    noun_list =[]
    with open(file_path,'r') as f:
        lines = f.readlines() # 한 라인씩 읽지 않으면 kn.nouns() 에서 에러남
        for line in lines:
            if km.nouns(line) != list(''):  
                nouns = km.nouns(line)
                for noun in nouns:
                    stopwords = get_stopwords()
                    if noun not in stopwords:
                        noun_list.append(noun)

    return(noun_list)
        
