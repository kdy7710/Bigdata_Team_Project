import urllib.request

urlString = 'https://avatars1.githubusercontent.com/u/44885477?s=460&v=4'
imageFromWeb = urllib.request.urlopen(urlString).read()
print(imageFromWeb)

 
