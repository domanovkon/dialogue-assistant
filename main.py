from telegram.ext import Updater, CommandHandler,RegexHandler, Filters, MessageHandler, ConversationHandler
from dialog.laptops import Laptop
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
            # "search":  [MessageHandler(Filters.all, Handler.search)],
            # "choose": [MessageHandler(Filters.all, Article.choose)],
            # "article": [MessageHandler(Filters.all, Article.defined)],
            # "defined": [MessageHandler(Filters.all, Article.defined)],
            # "undefined": [MessageHandler(Filters.all, Article.undefined)],
            # "show": [MessageHandler(Filters.all, Article.find)],
        },
        fallbacks=[MessageHandler(Filters.all, Handler.all_message)]
    ))

    dispatcher.add_handler(MessageHandler(Filters.all, Handler.all_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    start()
