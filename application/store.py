from ast import parse
from telebot import util
from application import bot
from model.chat import Chat


@bot.message_handler(commands=['save'])
def save(message):
    """
    Guarda un dato en el chat que se puede recuperar después
    """

    data = util.extract_arguments(message.text)
    if not data:
        bot.reply_to(
            message, "Debe indicar el dato que quiere que guarde", parse_mode='Markdown')
        return

    chat_id = message.chat.id
    Chat.set(chat_id, 'memory', data)
    bot.reply_to(message, "Dato guardado. Usa /load para recuperar",
                 parse_mode='Markdown')


@bot.message_handler(commands=['load'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    chat_id = message.chat.id
    data = Chat.get(chat_id, 'memory')
    if not data:
        bot.reply_to(message, "Aún no has guardado nada",
                     parse_mode='Markdown')
        return

    bot.reply_to(message, "Dato recuperado: %s" % data, parse_mode='Markdown')
