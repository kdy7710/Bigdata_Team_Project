from Kotube import get_info
<<<<<<< HEAD
from Youtube_URL import get_url
=======
from youtube_url_project import get_url
>>>>>>> df34a3239572f45eb14104809508f3e2a497f2c3
import pandas as pd
import numpy as np
import API_CLASS
import googletrend
import datetime
import json
from socialblade2 import socialblade1
<<<<<<< HEAD


def youtube_url_main(keyword, howmany):
    videolist = get_url(keyword,howmany)
    print(videolist)

df_raw = pd.read_pickle('glowpick_nodupl.pkl')
df = df_raw.copy()

result = pd.DataFrame(index=range(0,61))

for i, row in df.iterrows():
    keyword = row['상품명']
    # print(keyword)
    # print(type(keyword))
    url_list = get_url(keyword,3)
    for i in url_list:
        # print(i)
        # print(type(i))
        try:
            social_list = socialblade1(i)
        except:
            continue
        print(social_list)
        upload_date, sub = social_list[-2],social_list[-1] # upload_date, sub
        #시간설정
        today = API_CLASS.convert_strtime(upload_date)
        start_date , enddate = API_CLASS.timeminus(today, -30), API_CLASS.timeminus(today, 30)
        #네이버api
        na = API_CLASS.NaverApi(keyword,start_date , enddate).to_dataframe()
        googletrend.table_sub(na,sub)
        result[keyword]=na.reset_index(drop=True)
        print(result)
        
#        
result.to_csv('beauti_result1.csv',encoding='utf-8-sig')
=======
#from datetime import datetime
from tqdm import tqdm
import warnings
for i in range(0,24):
    warnings.filterwarnings("ignore")


    now = datetime.datetime.now()
    nowDate = str(now.strftime('%Y-%m-%d'))
    def youtube_url_main(keyword):
        videolist = get_url(keyword,3)
        print(videolist)

    num=i #파일번호
    num=str(num)
    df_raw = pd.read_csv('뷰티인플루언서 영향력 유튜브/split_data/na_result_'+num+'.csv')

    df = df_raw.copy()
    print(df.head())
    result_na = pd.DataFrame(index=range(0,62))
    result_goo = pd.DataFrame(index=range(0,62))

    for i, row in df.iterrows():
        print('[[첫번째 for문]]')
        print(i,'번 idx',row,'진행')
        keyword = row['상품명']
        # print(keyword)
        # print(type(keyword))
        url_list = get_url(keyword,10)
        iter_n = 0
        for i in tqdm(url_list):
            # print('[[두번째 for문]]')
            # print(i,'진행')
            # # print(i)
            # # print(type(i))
            # try:
            #     print('소셜 시작')
            #     social_list = socialblade1(i)
            #     print('소셜 끝+')
            # except:
            #     print('EXCEPT - in url_list')
            #     continue
            #print(social_list)
            upload_date, sub = i[0],i[1] # upload_date, sub
            
            upload_date = str(datetime.datetime.strptime(upload_date,'%Y-%m-%d').date())
            print(upload_date, sub)
            
            #시간설정
            today = API_CLASS.convert_strtime(upload_date)
            start_date , enddate = API_CLASS.timeminus(today, -30), API_CLASS.timeminus(today, 30)
            print(start_date, enddate)
            if enddate>=nowDate or start_date<'2016-01-01':
                print('CONTINUE - enddata >= nowDate')
                continue

            #네이버api
            print('[[#네이버 api" 진입]]')
            print(keyword,start_date , enddate)
            na = API_CLASS.NaverApi(keyword,start_date , enddate).to_dataframe()
            na = googletrend.table_sub(na,sub)
            print(na)
            result_na[keyword+'_'+str(iter_n)]=na.reset_index(drop=True)
            result_na.to_csv('beauti_result_na_'+num+'.csv',encoding='utf-8-sig')
            #print(result)

            #구글트렌드
            # try:
            #     goo = googletrend.googletrend(keyword,start_date , enddate)
            #     goo = googletrend.table_sub(goo,sub)
            #     result_goo[keyword]=goo.reset_index(drop=True)
            #     result_goo.to_csv('beauti_result_goo'+num+'.csv',encoding='utf-8-sig')
            # except:
            #     goo = googletrend.googletrend(keyword,start_date , enddate)
            #     goo = googletrend.table_sub(goo,sub)
            #     result_goo[keyword]=goo.reset_index(drop=True)
            #     result_goo.to_csv('beauti_result_goo'+num+'.csv',encoding='utf-8-sig')
            #print(result)

            iter_n +=1
            if iter_n>=3:
                print('BREAK - iter_n이 3이상')
                break
                
    #result.to_csv('beauti_result1.csv',encoding='utf-8-sig')
    print('완료')
>>>>>>> df34a3239572f45eb14104809508f3e2a497f2c3
