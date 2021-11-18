from telegram import ParseMode
from telegram.ext import ConversationHandler
from vocabulary.general import isMemeKeyword, isShowKeyword, isStopKeyword, isStockKeyword
from vocabulary.laptop import isLaptopKeyword
from standard_phrases import HEY_PHRASE, NOT_UNDERSTAND, BYE_PHRASE
from random import choice


class Handler:
    return_flag = True

    def __init__(self):
        self.message = None
        self.effective_chat = None

    def start(self, context):
        chat = self.effective_chat
        text = choice(HEY_PHRASE)
        self.message.reply_text(text.format(chat.first_name), parse_mode=ParseMode.MARKDOWN)
        return "general"

    def general(self, context):
        self.message.reply_text("Что я могу для тебя сделать?", parse_mode=ParseMode.MARKDOWN)
        return "all"

    def all(self, context):
        msg = self.message.text
        if isShowKeyword(msg) and isLaptopKeyword(msg):
            self.message.reply_text("Хорошо, показать весь список ноутбуков или подобрать какой-то конкретный?")
            return "laptop"
        elif isStockKeyword(msg) and isShowKeyword(msg):
            self.message.reply_text("Показать все акции магазина или ваши персональные предложения?")
            return "stock"
        elif isMemeKeyword(msg):
            self.message.reply_text("Хочите прикол? 😏")
            return "all"
        elif isStopKeyword(msg):
            self.message.reply_text(choice(BYE_PHRASE))
            return ConversationHandler.END
        else:
            self.message.reply_text(choice(NOT_UNDERSTAND))
            return "all"

    def all_message(self, context):
        msg = self.message.text
        self.message.reply_text(choice(NOT_UNDERSTAND))
