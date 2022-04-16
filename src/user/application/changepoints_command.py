# coding=utf-8
from application import bot
from utils.extract_arguments import extract_arguments_without_command
from src.league.domain.league import League
from src.user.domain.user import User


@bot.message_handler(commands=['changepoints'])
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

    if User.get(username, chatId) == None:
        bot.reply_to(
            message, "You are not registered in this league. Please make sure you are registered and you are the admin to use this command. 😬", parse_mode='Markdown')
        return None

    if User.is_admin(username, chatId) == False:
        bot.reply_to(
            message, "Sorry you are not the admin of this league. 😬", parse_mode='Markdown')
        return None

    arguments = extract_arguments_without_command(message.text)

    if User.get(arguments[0], chatId) == None:
        bot.reply_to(
            message, f"Make sure {arguments[0]} is the username of the person and also that it is registered in the league. Usage: /changepoints marc_doblefilo 7", parse_mode='HTML')
        return None

    if arguments[1].isdigit() == False:
        bot.reply_to(
            message, f"Make sure {arguments[1]} is the new points for the user. Usage: /changepoints marc_doblefilo 7", parse_mode='HTML')
        return None

    if int(arguments[1]) < 0:
        bot.reply_to(
            message, f"Make sure {arguments[1]} is equal or above 0. Usage: /changepoints marc_doblefilo 7", parse_mode='HTML')
        return None

    User.set_new_points(arguments[0], chatId, int(arguments[1]))
    bot.reply_to(message, f"Hurra!🥳 Now @{arguments[0]} has {arguments[1]} points.",
                 parse_mode='HTML')
