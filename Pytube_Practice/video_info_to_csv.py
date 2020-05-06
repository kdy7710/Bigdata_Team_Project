from Kotube import get_info
import pandas as pd
from Youtube_URL import get_url



df = pd.DataFrame(columns=['title','length','rating','thumbnail','views','description'])



videolist = get_url('도넛버거',30)

for i in range(0,len(videolist)):

    video_info = get_info(videolist[i])

    df = df.append({
        'title': video_info['title'],
        'length': video_info['length'],
        'rating': video_info['rating'],
        'thumbnail': video_info['thumbnail'],
        'views': video_info['views'],
        'description': video_info['description']
    }, ignore_index=True)



df.to_csv()
df.to_csv('burger.csv', encoding='utf-8-sig', index=False)