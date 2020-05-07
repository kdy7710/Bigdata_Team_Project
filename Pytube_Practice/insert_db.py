from Kotube import get_info
import pandas as pd
from Youtube_URL import get_url



df = pd.DataFrame(columns=['title','length','rating','thumbnail','views','description'])



videolist = get_url('도넛버거',30)

import pymysql
# alter charset to 'utf8mb4' to insert imoji
conn = pymysql.connect(host='localhost',user='bigdb',password='bigdb1234',db='bigdb',charset='utf8mb4')

cur = conn.cursor(pymysql.cursors.DictCursor)


for i in range(0,len(videolist)):
    
    video_info = get_info(videolist[i])
    print(type(video_info['description']))
    print(video_info['description'])
    sql = """
    insert into youtube 
    values (%s,%s,%s,%s,%s,%s,%s,now())
    """
    cur.execute(sql,
    (
        videolist[i], # url
        video_info['title'],
        video_info['length'],
        video_info['rating'],
        video_info['thumbnail'],
        video_info['views'],
        video_info['description']
    )
            )
   
    #sql문을 실행
    conn.commit()

conn.close()
