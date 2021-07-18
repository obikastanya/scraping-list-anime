from crawler import Crawler, ExcelWritter

url = 'https://myanimelist.net/topmanga.php'

listData=[]
for i in range(0,200, 50):
    limit='?limit='+str(i)
    newUrl=url+limit
    data=Crawler().getContent(newUrl)
    listData.extend(data)
    
ExcelWritter().createExcel(listData)