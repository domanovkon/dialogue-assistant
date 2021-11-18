import pymorphy2
import pandas as pd

PERSONAL = {"персональный", "мой", "свой", "я", "предложение"}

ALL_STOCKS = {"всё", "акции", "скидки", "магазин"}


def isPersonalKeyword(text):
    flag = False
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        print(wn)
        if wn in PERSONAL:
            flag = True
    return flag


def isAllStocksKeyword(text):
    flag = False
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        print(wn)
        if wn in ALL_STOCKS:
            flag = True
    return flag


def LoadAllStocksData():
    dataSetSearch = pd.read_csv('allStocks.txt', delimiter='\t', encoding="utf-16-le",
                                usecols=['Акция'])
    columns_titles = ["Акция"]
    dataSetSearch = dataSetSearch.reindex(columns=columns_titles)
    return dataSetSearch.values.tolist()


def LoadPersonalData():
    dataSetSearch = pd.read_csv('personal.txt', delimiter='\t', encoding="utf-16-le",
                                usecols=['Пользователь', 'Акция'])
    columns_titles = ["Пользователь", "Акция"]
    dataSetSearch = dataSetSearch.reindex(columns=columns_titles)
    return dataSetSearch.values.tolist()
