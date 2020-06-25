from Kotube import get_info
from youtube_url_project import get_url
import pandas as pd
import numpy as np
import API_CLASS
import googletrend
import datetime
import json
from socialblade2 import socialblade1
from datetime import datetime
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

now = datetime.now()
nowDate = str(now.strftime('%Y-%m-%d'))
def youtube_url_main(keyword):
    videolist = get_url(keyword,3)
    print(videolist)

num=30 #파일번호
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
        print('[[두번째 for문]]')
        print(i,'진행')
        # print(i)
        # print(type(i))
        try:
            print('소셜 시작')
            social_list = socialblade1(i)
            print('소셜 끝+')
        except:
            print('EXCEPT - in url_list')
            continue
        #print(social_list)
        upload_date, sub = social_list[-2],social_list[-1][-1] # upload_date, sub
        print(upload_date, sub)
        
        #시간설정
        today = API_CLASS.convert_strtime(upload_date)
        start_date , enddate = API_CLASS.timeminus(today, -30), API_CLASS.timeminus(today, 30)
        print(start_date, enddate)
        if enddate>=nowDate:
            print('CONTINUE - enddata >= nowDate')
            continue

        #네이버api
        print('[[#네이버 api" 진입]]')
        na = API_CLASS.NaverApi(keyword,start_date , enddate).to_dataframe()
        na = googletrend.table_sub(na,sub)
        print(na)
        result_na[keyword+'_'+iter_n]=na.reset_index(drop=True)
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