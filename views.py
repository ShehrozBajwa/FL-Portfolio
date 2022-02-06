from flask import Blueprint, render_template
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
views = Blueprint(__name__, "views")

ticker = ['AAPL', 'AMZN', 'MSFT', 'GME', 'VOO']
ticker1 = ['FB', 'ROKU', 'BABA', 'V', 'RY']


@views.route("/")
def home():
    return render_template("index.html", name="shehroz")


@views.route("/users")
def home1():
    nameList = []
    changeInPrice = []
    priceList = []
    percentList = []
    for i in range(0, len(ticker)):
        url = 'https://finance.yahoo.com/quote/%s' % ticker[i]
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        stockData = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all()
        stockName = soup.find('div', {
            'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find(
            'h1').text
        nameList.append(stockName)
        priceList.append(stockData[0].text.strip())
        changeInPrice.append(stockData[1].text.strip())
        percentList.append(stockData[3].text.strip())
    return render_template("users.html", name="shehroz",names=nameList,changeInPrice=changeInPrice, price=priceList, percent=percentList)

@views.route("/index1")
def home3():
    return render_template("index1.html", name="shehroz")


@views.route("/users1")
def home4():
    nameList = []
    changeInPrice = []
    priceList = []
    percentList = []
    for i in range(0, len(ticker1)):
        url = 'https://finance.yahoo.com/quote/%s' % ticker1[i]
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        stockData = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all()
        stockName = soup.find('div', {
            'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find(
            'h1').text
        nameList.append(stockName)
        priceList.append(stockData[0].text.strip())
        changeInPrice.append(stockData[1].text.strip())
        percentList.append(stockData[3].text.strip())
    return render_template("users1.html", name="shehroz",names=nameList,changeInPrice=changeInPrice, price=priceList, percent=percentList)
