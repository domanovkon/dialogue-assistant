import csv
import pandas as pd
import pymorphy2


FIND = {"найти", "находить", "отыскивать",  "подобрать", "выудить", "определить", "поиск", "искать"}

SHOW = {"показать", "показывать",  "представить", "демонстрировать", "предоставить", "покажите"}

STOP = {"хватит", "отвали", "ничего", "пока", "прекрати", "довольно", "перестань", "до свидания",
        "до встречи", "исчезни", "катись", "сгинь", "ничегошеньки"}


def isFindKeyword(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in FIND:
            flag = True
    return flag

def isShowKeyword(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in SHOW:
            flag = True
    return flag

def isStopKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        print(wn)
        if wn in STOP:
            flag = True
    return flag

def ReplaceSyn(text):
    text = text.replace("?", "")
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace(":", "")
    text = text.replace("!", "")
    return text

def LoadData():
    dataSetSearch = pd.read_csv('laptops.txt', delimiter='\t', encoding="utf-16-le",
                                usecols=['Тип видеокарты', 'Цена', 'Категория', 'Количество_ОЗУ', 'Процессор',
                                         'Ноутбук'])
    columns_titles = ["Ноутбук", 'Категория', 'Процессор', 'Количество_ОЗУ', "Тип видеокарты", 'Цена']
    dataSetSearch = dataSetSearch.reindex(columns=columns_titles)

    return dataSetSearch.values.tolist()
