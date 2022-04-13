# coding=utf-8
from application import bot
from model.league import League
from model.user import User
from telebot.types import Message


@bot.message_handler(commands=['register'])
def register(message):
    chatId = message.chat.id
    userId = message.from_user.username
    chatName = message.chat.title

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. I can not register you in any league. Please use this command in a group 😔", parse_mode='Markdown')
        return

    if League.get(chatId) == None:
        bot.reply_to(
            message, "There is no league in this group yet. Use the command /startleague to start it! 😎", parse_mode='Markdown')
        return

    if User.get(userId, chatId):
        bot.reply_to(
            message, "You are already registered in this league. Enjoy your predictions! 😎", parse_mode='Markdown')
        return

    User.set(chatId, chatName)
    bot.reply_to(message, "You are now registered in this league. Enjoy %s 🥳" % message.from_user.first_name,
                 parse_mode='Markdown')
