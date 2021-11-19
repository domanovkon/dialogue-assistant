from telegram.ext import Updater, CommandHandler, RegexHandler, Filters, MessageHandler, ConversationHandler
from dialog.laptops import Laptop
from dialog.stocks import Stock
from dialog.memes import Memes
from dialog.games import Game
from token_api import TOKEN_API
from dialog.general import Handler


updater = Updater(TOKEN_API, use_context=True)
dispatcher = updater.dispatcher


def start():
    dispatcher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.all, Handler.start, pass_user_data=True)],
        states={
            "general": [MessageHandler(Filters.all, Handler.general)],
            "all": [MessageHandler(Filters.all, Handler.all)],
            "laptop": [MessageHandler(Filters.all, Laptop.find)],
            "laptopName": [MessageHandler(Filters.all, Laptop.findByName)],
            "stock": [MessageHandler(Filters.all, Stock.findStocks)],
            "memes": [MessageHandler(Filters.all, Memes.showMemes)],
            "game": [MessageHandler(Filters.all, Game.startGame)],
            "play": [MessageHandler(Filters.all, Game.play)]
        },
        fallbacks=[MessageHandler(Filters.all, Handler.all_message)]
    ))

    dispatcher.add_handler(MessageHandler(Filters.all, Handler.all_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    start()
