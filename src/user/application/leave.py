# coding=utf-8
from application import bot
from src.league.domain.league import League
from src.user.domain.user import User


@bot.message_handler(commands=['leave'])
def register(message):
    chatId = message.chat.id
    username = message.from_user.username

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. Please use this command in a group 😔", parse_mode='Markdown')
        return None

    if League.get(chatId) == None:
        bot.reply_to(
            message, "There is no league in this group yet. Use the command /startleague to start it! 😎", parse_mode='Markdown')
        return None

    if User.get(username, chatId) == None:
        bot.reply_to(
            message, "You are not in this league. Remember to use /register if you want to play again 😊", parse_mode='Markdown')
        return None

    if User.is_admin(username, chatId):
        bot.reply_to(
            message, "You can not leave this league as you are the admin. 😓", parse_mode='Markdown')
        return None

    User.remove(username, chatId)
    bot.reply_to(message, "We will miss you. You are not in %s league anymore 😭" % League.get(chatId).leagueName,
                 parse_mode='Markdown')
