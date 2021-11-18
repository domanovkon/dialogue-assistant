import pymorphy2

from vocabulary.general import ReplaceSyn

YES = {"да", "верно", "правильно", "отлично", "точно", "определённо", "ясно", "ага", "угу", "yes"}

NO = {"нет", "не", "неа", "no"}

def isYesKeyword(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in YES:
            flag = True
    return flag


def isNoKeyword(text):
    flag = False
    text = ReplaceSyn(text)
    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        if wn in NO:
            flag = True
    return flag
