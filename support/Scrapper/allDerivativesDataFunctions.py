import requests
import json
import psycopg2
from retry import retry
from bs4 import BeautifulSoup

conn = psycopg2.connect(
    host = "localhost",
    database = "rawscrappeddata",
    user = "postgres",
    password = "1234"
)

csr = conn.cursor()

@retry()
def getAllOptionContracts():
    niftyUrl = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
    bankNiftyUrl = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'

    header = {
          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
          "X-Requested-With": "XMLHttpRequest"
        }
    while True:
        niftyRequest = requests.get(niftyUrl, headers = header, timeout = 10)
        if niftyRequest.status_code == 200:
            break
    while True:
        bankNiftyRequest = requests.get(bankNiftyUrl, headers = header, timeout = 10)
        if bankNiftyRequest.status_code == 200:
            break
    niftySoup = json.loads(str(BeautifulSoup(niftyRequest.text, 'html.parser')))
    bankNiftySoup = json.loads(str(BeautifulSoup(bankNiftyRequest.text, 'html.parser')))

    rawOptionData = []

    for indexName in (niftySoup['records']['data'], bankNiftySoup['records']['data']):
        for optionData in indexName:
            try:
                if 0 not in optionData['PE'].values():
                    optionData['PE']['optType'] = 'PE'
                    rawOptionData.append(optionData['PE'])
                else:
                    pass
            except:
                pass
                
            try:
                if 0 not in optionData['CE'].values():
                    optionData['CE']['optType'] = 'CE'
                    rawOptionData.append(optionData['CE'])
                else:
                    pass
            except:
                pass

    return rawOptionData