import psycopg2
from datetime import datetime

from support.Scrapper.allTickerDataFunctions import dataFromAllStreams
from support.Scrapper.allNewsDataFunctions import getAllNewArticles
from support.Scrapper.allDerivativesDataFunctions import getAllOptionContracts

conn = psycopg2.connect(
    host = "localhost",
    database = "rawscrappeddata",
    user = "postgres",
    password = "1234",
    port = 5432
)
csr = conn.cursor()

class Scrapper:
    def __init__(self):
        self.tickerInsertString = f"INSERT INTO tickerdata VALUES(%s, %s, %s)"
        self.newsInsertString = f"INSERT INTO newsdata VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        self.derivativesInsertString = f"INSERT INTO derivativesdata VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
        self.last1hNewsTitlesList = []
        self.lastTimestamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:00'))

    def getTickerData(self):
        tickerData = dataFromAllStreams()
        return tickerData

    def getNewsData(self):
        newsData, self.last1hNewsTitlesList = getAllNewArticles(last1hNewsTitlesList = self.last1hNewsTitlesList)
        return newsData

    def getDerivativesData(self):
        derivativesData = getAllOptionContracts()
        return derivativesData

    def insertTickerData(self):
        tickerData = Scrapper.getTickerData(self)
        for singleTicker in tickerData:
            csr.execute(self.tickerInsertString, (self.newTimestamp, singleTicker.get('ticker'), str(singleTicker.get('close')).replace(",", "")))
        conn.commit()

    def insertNewsData(self):
        newsData = Scrapper.getNewsData(self)
        for singleArticle in newsData:
            csr.execute(self.newsInsertString, (self.newTimestamp, singleArticle['title'], singleArticle['dateTimePublished'], singleArticle['link'], singleArticle['text'], singleArticle['keywords'], singleArticle['summary'], singleArticle['author']))
        conn.commit()
        return len(newsData)

    def insertDerivativesData(self):
        derivativesData = Scrapper.getDerivativesData(self)
        for singleContract in derivativesData:
            csr.execute(self.derivativesInsertString, (self.newTimestamp, singleContract['underlying'], singleContract['expiryDate'], singleContract['optType'], singleContract['strikePrice'], singleContract['underlyingValue'], singleContract['openInterest'], singleContract['totalTradedVolume'], singleContract['impliedVolatility'], singleContract['lastPrice'], singleContract['bidprice'], singleContract['askPrice']))
        conn.commit()
        return len(derivativesData)
        
    def getAndStoreData(self):
        while True:
            self.newTimestamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:00'))
            # if datetime.today().weekday() < 5 and datetime.now().strftime('%H:%M') > '08:45' and datetime.now().strftime('%H:%M') < '16:01':
            #     if int(datetime.now().strftime('%M'))%5 == 0 and self.newTimestamp > self.lastTimestamp:
            if self.newTimestamp > self.lastTimestamp:
                if self.newTimestamp > self.lastTimestamp:
                    totalNumberOfContracts = Scrapper.insertDerivativesData(self)
                    print(f"{totalNumberOfContracts} Contracts were inserted at {self.newTimestamp}")
                else:
                    pass
                if self.newTimestamp > self.lastTimestamp:
                    Scrapper.insertTickerData(self)
                    print(f"Ticker Data inserted for {self.newTimestamp}")
                    totalNewArticles = Scrapper.insertNewsData(self)
                    print(f"{totalNewArticles} Aritlces were inserted at {self.newTimestamp}")
                    self.lastTimestamp = self.newTimestamp
                else:
                    pass

_ = Scrapper()
_.getAndStoreData()