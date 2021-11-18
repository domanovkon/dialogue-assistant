import pymorphy2

LAPTOP = {"ноутбук", "ноут", "ультрабук", "компьютер",
           "комп", "ЭВМ", "отчёт", "лэптоп", "нетбук", "нотбук", "компуктер", "компудахтер", "миникомпьютер",
           "макинтош", "персоналка", "пк", "компис", "товар", "инвентарь", "продукт", "продукция", "ассортимент"}

ALL = {"все", "весь", "ассортимент", "список", "несколько", "много", "каталог"}

ONE = {"один", "конкретный", "только", "единственный"}

def isLaptopKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        print(wn)
        if wn in LAPTOP:
            flag = True
    return flag

def isAllKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        print(wn)
        if wn in ALL:
            flag = True
    return flag


def isOneKeyword(text):
    flag = False

    morph = pymorphy2.MorphAnalyzer()
    words = text.split()
    for w in words:
        wn = morph.parse(w)[0].normal_form
        print(wn)
        if wn in ONE:
            flag = True
    return flag