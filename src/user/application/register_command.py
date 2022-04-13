# coding=utf-8
from application import bot
from src.league.domain.league import League
from src.user.domain.user import User


@bot.message_handler(commands=['register'])
def register(message):
    chatId = message.chat.id
    username = message.from_user.username

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. I can not register you in any league. Please use this command in a group 😔", parse_mode='Markdown')
        return None

    if League.get(chatId) == None:
        bot.reply_to(
            message, "There is no league in this group yet. Use the command /startleague to start it! 😎", parse_mode='Markdown')
        return None

    if User.get(username, chatId):
        bot.reply_to(
            message, "You are already registered in this league. Enjoy your predictions! 😎", parse_mode='Markdown')
        return None

    User.set(username, chatId)
    bot.reply_to(message, "You are now registered in this league. Enjoy %s 🥳" % message.from_user.first_name,
                 parse_mode='Markdown')
