from vocabulary.general import LoadData
from smiles import sml
from telegram import ParseMode
from telegram.ext import ConversationHandler
from vocabulary.laptop import isOneKeyword, isAllKeyword
from standard_phrases import NOT_UNDERSTAND
from random import choice


class Laptop:
    def __init__(self):
        self.message = None
        self.effective_chat = None

    def find(self, context):
        msg = self.message.text
        if isAllKeyword(msg):
            laptop_list = LoadData()
            laptop_list_counter = 0
            for x in laptop_list:
                laptop_list_counter = laptop_list_counter + 1
                str1 = x[0] + "\n" + "Категория: " + x[1] + "\n" + "Процессор: " + x[2] + "\n" + \
                       "Количество ОЗУ: " + str(x[3]) + "\n" + "Тип видеокарты: " + x[4] + "\n" + "Цена: " + x[5]
                self.message.reply_text(sml[laptop_list_counter] + " " + str1 + " 😎")
            self.message.reply_text("Что еще для вас сделать?", parse_mode=ParseMode.MARKDOWN)
            return "all"
        elif isOneKeyword(msg):
            self.message.reply_text("Один ноутбук")
            return ConversationHandler.END
        else:
            self.message.reply_text(choice(NOT_UNDERSTAND))
            return "laptop"
