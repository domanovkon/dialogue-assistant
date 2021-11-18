from vocabulary.meme import isYesKeyword, isNoKeyword
from random import choice
from standard_phrases import NOT_UNDERSTAND


class Game:
    def __init__(self):
        self.message = None
        self.effective_chat = None

    def startGame(self, context):
        msg = self.message.text
        if isYesKeyword(msg):
            self.message.reply_text("Отлично, я загадываю !!!")
            return 0
        elif isNoKeyword(msg):
            self.message.reply_text("Ну и ладно, не особо то и хотелось")
            self.message.reply_text("Чем еще могу вам помочь?")
            return "all"
        else:
            self.message.reply_text(choice(NOT_UNDERSTAND))
            return "game"
