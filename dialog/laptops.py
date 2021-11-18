from vocabulary.general import LoadData
from smiles import sml
from telegram import ParseMode
from telegram.ext import ConversationHandler
from vocabulary.laptop import isOneKeyword, isAllKeyword, findByName
from standard_phrases import NOT_UNDERSTAND, NOT_FOUND
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
            self.message.reply_text("Ищем по названию ноутбука 🔡")
            return "laptopName"
        else:
            self.message.reply_text(choice(NOT_UNDERSTAND))
            return "laptop"

    def findByName(self, context):
        msg = self.message.text
        laptop = findByName(msg)
        if not laptop:
            self.message.reply_text(choice(NOT_FOUND))
            return "laptopName"
        else:
            str1 = laptop[0] + "\n\nХарактеристики товара 💪" + "\n" + "Категория: " + laptop[1] + "\n" + "Процессор: " + laptop[2] + "\n" + \
                   "Количество ОЗУ: " + str(laptop[3]) + "\n" + "Тип видеокарты: " + laptop[4] + "\n" + "Цена: " + laptop[5]
            self.message.reply_text(str1 + " 😎")
            self.message.reply_text("Чем я еще могу помочь?", parse_mode=ParseMode.MARKDOWN)
        return "all"
