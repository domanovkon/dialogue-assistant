import pandas as pd
import pymorphy2

from vocabulary.general import ReplaceSyn

STOP_GAME = {"хватить", "отвалить", "пока", "перестать", "прекратить", "довольно", "перестать",
             "исчезнуть", "катиться", "сгинуть", "конец", "закончить", "сдаваться", "устать"}


def isStopGameKeyword(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in STOP_GAME:
            flag = True
    return flag


def LoadCityData():
    dataSetSearch = pd.read_csv('city.txt', delimiter='\t', encoding="utf-16-le",
                                usecols=['name'])
    temp = []
    for x in dataSetSearch.values.tolist():
        temp.append(x[0])
    return temp
