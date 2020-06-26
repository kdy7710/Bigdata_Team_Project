"""
db 연결 후 데이터 insert 예제 
"""
from Kotube import get_info
from Youtube_URL import get_url



videolist = get_url('파이썬',30)
for i in videolist:
    print(i)

