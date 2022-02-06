from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import datetime, time

channel_id = 847298157753794623
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
ticker = input()

def view(ticker):
    stockPriceOutput = ""
    url = 'https://finance.yahoo.com/quote/%s' % ticker
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stockData = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all()
    stockName = soup.find('div', {
            'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find(
            'h1').text
    currPrice = stockData[0].text.strip()
    changeInPrice = stockData[1].text.strip()
    percent = stockData[3].text.strip()
    stockPriceOutput += "%s:\n    Current Price: %s \n    Change in Price: %s %s \n" % (stockName, currPrice, changeInPrice, percent)
    return stockPriceOutput


print(view(ticker))
