from vocabulary.meme import isYesKeyword, isNoKeyword
from standard_phrases import MEME
from random import choice
from standard_phrases import NOT_UNDERSTAND


class Memes:
    def __init__(self):
        self.message = None
        self.effective_chat = None

    def showMemes(self, context):
        msg = self.message.text
        if isYesKeyword(msg):
            self.message.reply_text(choice(MEME))
            self.message.reply_text("АХАХАХАХХАХАХХАХ 😂😂😂")
            self.message.reply_text("Чем еще могу вам помочь?")
            return "all"
        elif isNoKeyword(msg):
            self.message.reply_text("Ну ладно, прикола не будет :(")
            self.message.reply_text("Чем еще могу вам помочь?")
            return "all"
        else:
            self.message.reply_text(choice(NOT_UNDERSTAND))
            return "memes"
