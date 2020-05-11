import csv
content = ''
with open('C:/Users/TT_L/Desktop/2020-04-21_17-44-30.csv','r',encoding='UTF8') as f:
    reader = csv.reader(f)



    for txt in reader:
        content += txt[4]












