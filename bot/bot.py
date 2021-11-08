import telegram
from . import bot_settings


def send_visitor_message(message):
    mybot = telegram.Bot(bot_settings.API_KEY)
    mybot.send_message(bot_settings.CHAT_ID, text=message)
