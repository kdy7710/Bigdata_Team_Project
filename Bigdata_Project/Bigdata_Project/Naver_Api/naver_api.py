def search(keyword1, startdate = '2020-01-01', enddate = '2020-03-01' ):
    """
    Naver_api 이용해서 검색후 
    날짜와 검색율 가진 Dataframe을 Return
    (네이버 API 상에서 해당 날짜 값이 없을 시 아무 값도 
    리턴 하지 않으므로 임의로 해당날짜에 값 0 삽입)
    데이터가 0인 날은 missing date 리스트로 출력.
    
    """

    import os
    import re 
    import sys
    import pandas as pd
    import urllib.request
 
    dt_index = pd.date_range(start=startdate, end=enddate)
    dt_list = dt_index.strftime("%Y%m%d").tolist()
    


    # 네이버 API 접근 계정
    client_id = "I4Fva_A2tRCvTccEOaAX"
    client_secret = "jC5ic5g9wu"

    # URL
    url = "https://openapi.naver.com/v1/datalab/search"

    # 질의문
    body = "{\"startDate\":\"%s\",\
             \"endDate\":\"%s\",\
             \"timeUnit\":\"date\",\
             \"keywordGroups\":[{\
             \"groupName\":\"%s\",\
             \"keywords\":[\"%s\"]}]}" %(startdate,enddate,keyword1,keyword1)

    # 초기화
    regexp_date = ''  # 날짜 정규식 적용
    regexp_ratio= ''  # 비율 정규식 적용
    union_date=""     # 날짜 정규식 결과값 결합
    result_date = []  # String -> List 변환
    result_ratio = [] # String -> List 변환
    union_date_ratio =[] # 날짜와 비율을 같은 인덱스에 담기 위한 리스트

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):

        # 네이버API 질의문에 대한 응답 리스트에 저장 (인코딩, 쉼표 기준 문자열 자르기)
        response_body = response.read().decode('utf-8').split(',')

        # print(response_body)
        
        # print(len(response_body))
       
        for i in range(0,len(response_body)) :
            #정규식(날짜) 적용하여 필터링된 값 저장
            regexp_date = re.findall('\d{4}-\d\d-\d\d',response_body[i])
            regexp_date = str(regexp_date).replace("['",'')
            regexp_date = regexp_date.replace("']",'')

            if regexp_date != '[]':
                result_date.append(str(regexp_date)) 

        # result_date에서 시작&끝 날짜 제외
        result_date = result_date[2:]



        for i in range(0,len(response_body)) :
            #정규식(비율->실수) 적용하여 필터링된 값 저장
            #100이 나오는 경우가 있어 정규식에 포함
            rate = re.compile(':\d{1,3}')
            regexp_ratio = re.findall('\d+\.\d+',response_body[i])
            if regexp_ratio == list(''):
                regexp_ratio = re.findall(rate,response_body[i])
            if regexp_ratio!=list(''):
                #리스트가 비어있지 않을 경우에만 저장
                regexp_ratio = str(regexp_ratio).replace("['",'')
                regexp_ratio = str(regexp_ratio).replace("']",'')
                regexp_ratio = str(regexp_ratio).replace(":",'')
                result_ratio.append(regexp_ratio)


    else:
        print("Error Code:" + rescode)
    
    for idx,i in enumerate(result_date):
        result_date[idx] = i.replace('-','')
    
    # rate 없는 날짜 리스트 만들기 
    missing_date = []
    for i in range(1,len(dt_list)):
        if dt_list[i] not in result_date:
            missing_date.append(dt_list[i])
            

    
    df = pd.DataFrame(union_date_ratio, columns=['날짜','비율'])
    for i in range(0,len(result_ratio)):
        df = df.append(
        {
            '날짜' : result_date[i],
            '비율' : result_ratio[i]

        }, ignore_index=True 
        )
     

    # 전체 날짜 가지고 있는 값없는 df
    df2 = pd.DataFrame(union_date_ratio, columns=['날짜','비율'])
    for i in range(0,len(dt_list)):
            df2 = df2.append(
            {
                '날짜': dt_list[i]
            }, ignore_index=True 
            )
     

    df_final = pd.merge(df,df2,on='날짜',how='right')
    df_final = df_final.sort_values(['날짜'],ascending=[True])
    df_final = df_final.drop('비율_y',axis=1)
    
    df_final = df_final.set_index('날짜')
    df_final=df_final.astype(float).fillna(0)

    print("missing_dates :{}".format(missing_date))

    

    return(df_final)
    

if __name__ == '__main__':
    a= search(keyword1='원통젠가',startdate='2019-04-01',enddate='2019-05-31')
     