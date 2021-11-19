from vocabulary.meme import isYesKeyword, isNoKeyword
from standard_phrases import NOT_UNDERSTAND, GAME_TOWN_CALLED, GAME_TOWN_NOT_EXIST
from vocabulary.game import LoadCityData, isStopGameKeyword
from random import choice

cities = []
called = []

class Game:
    def __init__(self):
        self.message = None
        self.effective_chat = None

    def startGame(self, context):
        msg = self.message.text
        if isYesKeyword(msg):
            self.message.reply_text("Отлично, я начинаю !")
            global cities
            cities = LoadCityData()
            my_town = choice(cities)
            cities.remove(my_town)
            called.append(my_town)
            self.message.reply_text(my_town)
            return "play"
        elif isNoKeyword(msg):
            self.message.reply_text("Ну и ладно, не особо то и хотелось")
            self.message.reply_text("Чем еще могу вам помочь?")
            return "all"
        else:
            self.message.reply_text(choice(NOT_UNDERSTAND))
            return "game"

    def play(self, context):
        msg = self.message.text
        if isStopGameKeyword(msg):
            called.clear()
            self.message.reply_text("Так уж и быть, приму твое поражение 😎")
            self.message.reply_text("Чем еще могу вам помочь?")
            return "all"
        else:
            mes = str(msg).lower()
            flag = 0
            temp_city = ""
            my_city = []
            last_word = called[len(called) - 1]
            print(last_word)
            print(last_word)
            if mes[0] != last_word[-1]:
                self.message.reply_text("Придумайте слово на букву " + last_word[-1].upper())
                return "play"
            for x in cities:
                if mes == str(x).lower():
                    flag = 1
                    temp_city = x
            for x in called:
                if mes == str(x).lower():
                    flag = 2
            if flag == 1:
                cities.remove(temp_city)
                called.append(temp_city)
                last = temp_city[len(temp_city)-1]
                for x in cities:
                    if str(x)[0].lower() == last:
                        my_city.append(x)
                if (len(my_city) == 0):
                    self.message.reply_text("Я не знаю городов на букву " + last.upper() + " :(\nПоздравляю с победой!")
                    self.message.reply_text("Что будем делать дальше?")
                    return "all"
                else:
                    my_c = choice(my_city)
                    cities.remove(my_c)
                    called.append(my_c)
                    self.message.reply_text(my_c)
                return "play"
            elif flag == 2:
                self.message.reply_text(choice(GAME_TOWN_CALLED))
                return "play"
            else:
                self.message.reply_text(choice(GAME_TOWN_NOT_EXIST))
                return "play"

