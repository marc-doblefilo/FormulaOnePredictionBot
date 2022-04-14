# coding=utf-8
from application import bot
from src.league.domain.league import League


@bot.message_handler(commands=['help'])
def start(message):
    chatId = message.chat.id

    if chatId > 0:
        bot.reply_to(
            message, "This is not a group. Please use me only in groups 😔", parse_mode='Markdown')
        return

    help_message = "Hi %s👋. These are all the available commands: \n" +\
        "*BASIC* \n" +\
        "    /startleague - To start a league in any group.\n" +\
        "    /drivers - See all current driver.\n" +\
        "    /help - See this message.\n" +\
        "\n*LEAGUE* \n" +\
        "    /register - You will be registered.\n" +\
        "    /standings - See the current standings.\n" +\
        "    /leave - You will leave the league.\n"

    bot.send_message(message.chat.id, help_message %
                     message.from_user.first_name, parse_mode='Markdown')
