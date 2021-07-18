from bs4 import BeautifulSoup
import requests
import xlsxwriter

class Crawler():
    def __init__(self):
        pass

    def getContent(self,url):
        req=requests.get(url)
        page=req.text
        soup=BeautifulSoup(page, 'lxml')
        data=soup.select('tr.ranking-list')
        ListDictData=[]
        for item in data:
            rank=item.select('td .top-anime-rank-text')
            title=item.select('div.detail h3 a')
            score=item.select('td.score span.score-label')
            tempDict={
                'rank':rank[0].string,
                'title':title[0].string,
                'score':score[0].string
            }
            ListDictData.append(tempDict)
        return ListDictData


class ExcelWritter():
    def __init__(self):
        self.workbook=xlsxwriter.Workbook('excel/topAnime.xlsx')
        self.worksheet=self.workbook.add_worksheet()

    def wHeader(self,header):
        self.worksheet.write_row(1,0, header)

    def wData(self,data):
        for i,item in enumerate(data,start=2):
            self.worksheet.write(i,0,item.get('rank'))
            self.worksheet.write(i,1,item.get('title'))
            self.worksheet.write(i,2,item.get('score'))

    def createExcel(self, data):
        header=['Peringkat','Judul','Skor']
        self.wHeader(header)
        self.wData(data)
        self.workbook.close()