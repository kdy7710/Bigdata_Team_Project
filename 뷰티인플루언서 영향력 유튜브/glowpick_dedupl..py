import pandas as pd

# all_brand_name.xlsx ['상품명'] 중복 제거
"""
glowpick.ipynb에 삽입되는 것이 좋을 것 같습니다.
(glowpick을 다시 실행하기가 힘들 것 같아서 결과물을 불러와서 진행했습니다.)
"""

df = pd.read_excel('all_brand_name.xlsx', sheet_name='Sheet1')
df = df.drop_duplicates(['상품명'])
<<<<<<< HEAD
ew = pd.ExcelWriter('dedupl_brand_name.xlsx', engine='xlsxwriter')
df.to_excel(ew, index=False)
ew.save()
ew.close()
=======
print(df.unique())
# ew = pd.ExcelWriter('dedupl_brand_name.xlsx', engine='xlsxwriter')
# df.to_excel(ew, index=False)
# ew.save()
# ew.close()
>>>>>>> df34a3239572f45eb14104809508f3e2a497f2c3
