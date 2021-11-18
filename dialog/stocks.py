from vocabulary.stock import isAllStocksKeyword, isPersonalKeyword, LoadAllStocksData, LoadPersonalData
from standard_phrases import NOT_UNDERSTAND
from random import choice
from smiles import sml


class Stock:
    def __init__(self):
        self.message = None
        self.effective_chat = None

    def findStocks(self, context):
        msg = self.message.text
        if isAllStocksKeyword(msg):
            stocks = LoadAllStocksData()
            stock_list_counter = 0
            if len(stocks) == 0:
                self.message.reply_text("Список акций магазина пуст  😞")
            else:
                for x in stocks:
                    stock_list_counter = stock_list_counter + 1
                    self.message.reply_text(sml[stock_list_counter] + " " + x[0] + " ❗\n")
            self.message.reply_text("Чем еще могу помочь?")
            return "all"
        elif isPersonalKeyword(msg):
            personals = LoadPersonalData()
            personals_list_counter = 0
            if len(personals) == 0:
                self.message.reply_text("У вас нет персональных предложений  😞")
            else:
                self.message.reply_text("Предложения для " + self.effective_chat.username)
                for x in personals:
                    if x[0] == self.effective_chat.username:
                        personals_list_counter = personals_list_counter + 1
                        self.message.reply_text(sml[personals_list_counter] + " " + x[1] + " ❗\n")
            self.message.reply_text("Чем еще могу быть полезен?")
            return "all"
        else:
            self.message.reply_text(choice(NOT_UNDERSTAND))
            return "stock"
