# coding=utf-8
from application import bot
from src.league.domain.league import League
from src.user.domain.user import User


@bot.message_handler(commands=['removeleague'])
def remove_league(message):
    chatId = message.chat.id
    username = message.from_user.username

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. Please use me only in groups 😔", parse_mode='Markdown')
        return

    if League.get(chatId) == None:
        bot.reply_to(
            message, "There is no league in this group. Use /startleague to start one! 😎", parse_mode='Markdown')
        return

    if User.is_admin(username, chatId) == False:
        bot.reply_to(
            message, "Sorry you are not the admin of this league. 😬", parse_mode='Markdown')
        return

    User.remove_all_from_league(chatId)
    League.remove(chatId)
    bot.reply_to(message, "This league was removed. If you want to start it again, user /startleague 👋😭",
                 parse_mode='Markdown')
