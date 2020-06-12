from Kotube import get_ko_sub
from Youtube_URL import get_url


videolist = get_url('달고나커피',20)

text = ''
for i in range(0,len(videolist)):
    text += get_ko_sub(videolist[i])

print(text)
