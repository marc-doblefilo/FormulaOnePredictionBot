# coding=utf-8
from application import bot
from infrastructure.get_drivers import get_current_drivers
from model.league import League
from shared.tables import create_drivers_table


@bot.message_handler(commands=['getdrivers'])
def start(message):
    chatId = message.chat.id

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. Please use me only in groups 😔", parse_mode='Markdown')
        return

    response = get_current_drivers()
    table = create_drivers_table(response)

    bot.reply_to(message, f'<pre>{table}</pre>',
                 parse_mode='HTML')
