from Kotube import get_info
from Youtube_URL import get_url



videolist = get_url('파이썬',30)

import pymysql
# alter charset to 'utf8mb4' to insert imoji
conn = pymysql.connect(host='13.58.15.95', port= 3306, user='Habeen',password='jih4412',db='test')

cur = conn.cursor(pymysql.cursors.DictCursor)


for i in range(0,len(videolist)):
    
    video_info = get_info(videolist[i])

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
