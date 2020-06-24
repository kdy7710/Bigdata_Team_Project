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
now = datetime.now()
nowDate = str(now.strftime('%Y-%m-%d'))
def youtube_url_main(keyword):
    videolist = get_url(keyword,3)
    print(videolist)
df_raw = pd.read_csv('뷰티인플루언서 영향력 유튜브/split_data/na_result_0.csv')

df = df_raw.copy()

result_na = pd.DataFrame(index=range(0,62))
result_goo = pd.DataFrame(index=range(0,62))

for i, row in df.iterrows():
    keyword = row['상품명']
    # print(keyword)
    # print(type(keyword))
    url_list = get_url(keyword,10)
    iter_n = 0
    for i in url_list:
        # print(i)
        # print(type(i))
        try:
            social_list = socialblade1(i)
        except:
            continue
        #print(social_list)
        upload_date, sub = social_list[-2],social_list[-1][-1] # upload_date, sub
        #print(upload_date, sub)
        
        #시간설정
        today = API_CLASS.convert_strtime(upload_date)
        start_date , enddate = API_CLASS.timeminus(today, -30), API_CLASS.timeminus(today, 30)
        if enddate>=nowDate:
            continue

        #네이버api
        na = API_CLASS.NaverApi(keyword,start_date , enddate).to_dataframe()
        na = googletrend.table_sub(na,sub)
        result_na[keyword]=na.reset_index(drop=True)
        result_na.to_csv('beauti_result_na.csv',encoding='utf-8-sig')
        #print(result)

        #구글트렌드
        # try:
        #     goo = googletrend.googletrend(keyword,start_date , enddate)
        #     goo = googletrend.table_sub(goo,sub)
        #     result_goo[keyword]=goo.reset_index(drop=True)
        #     result_goo.to_csv('beauti_result_goo.csv',encoding='utf-8-sig')
        # except:
        #     goo = googletrend.googletrend(keyword,start_date , enddate)
        #     goo = googletrend.table_sub(goo,sub)
        #     result_goo[keyword]=goo.reset_index(drop=True)
        #     result_goo.to_csv('beauti_result_goo.csv',encoding='utf-8-sig')
        #print(result)

        iter_n +=1
        if iter_n>=3:
            break
               
#result.to_csv('beauti_result1.csv',encoding='utf-8-sig')
print('완료')