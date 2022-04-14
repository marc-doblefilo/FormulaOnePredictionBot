# coding=utf-8
from application import bot
from src.league.domain.league import League
from src.user.domain.user import User


@bot.message_handler(commands=['startleague'])
def start(message):
    chatId = message.chat.id
    chatName = message.chat.title
    userId = message.from_user.username

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. I can not create a league 😔", parse_mode='Markdown')
        return

    if League.get(chatId):
        bot.reply_to(
            message, "This League was already created. Enjoy your predictions! 😎", parse_mode='Markdown')
        return

    League.set(chatId, chatName)
    User.set_user_as_admin(userId, chatId)
    bot.reply_to(message, "A new League was created: %s." % League.get(chatId).leagueName,
                 parse_mode='Markdown')
