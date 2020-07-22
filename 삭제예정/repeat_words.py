def repeat_word(repeat_num, sub_wordlist 자막리스트2중리스트)
"""
 def repeat_word(몇번중복이상, 자막리스트2중리스트
 return 중복단어 리스트
"""
    dic = {}
    for i in range(len(sub_wordlist)):
        for j in range(len(sub_wordlist[i])):
            dic[i] = dic.setdefault(sub_wordlist[i][j],0)+1    
        repeat_words=[]
    for i in dic:
        if dic[i]>=repeat_num:
            repeat_words.append(dic[i])
        else:
            continue

    
return repeat_words