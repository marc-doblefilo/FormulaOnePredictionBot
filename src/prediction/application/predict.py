# coding=utf-8
from application import bot
from src.prediction.domain.prediction import Prediction
from src.race.domain.race import Race
from src.driver.infrastructure.get_code_drivers import get_current_drivers_code
from utils.extract_arguments import extract_arguments_without_command
from src.league.domain.league import League
from src.user.domain.user import User


@bot.message_handler(commands=['predict'])
def predict(message):
    chat_id = message.chat.id
    username = message.from_user.username

    if chat_id > 0:
        bot.reply_to(
            message, "This is not a group. I can not register you in any league. Please use this command in a group 😔", parse_mode='Markdown')
        return

    if League.get(chat_id) == None:
        bot.reply_to(
            message, "There is no league in this group yet. Use the command /startleague to start it! 😎", parse_mode='Markdown')
        return

    if User.get(username, chat_id) == None:
        bot.reply_to(
            message, "You are not registered in this league. Please make sure you are registered and you are the admin to use this command. 😬", parse_mode='Markdown')
        return

    if Race.get_current_race() != None:
        bot.reply_to(
            message, "Sorry buddy, predictions are closed waiting for the current race to finish😬. Enjoy the race🏁", parse_mode='Markdown'
        )
        return

    arguments = extract_arguments_without_command(message.text)

    if len(arguments) != 3:
        bot.reply_to(
            message, "I can't understand that message😓, please use the code (ALO) of the drivers. Usage: /predict LEC VER ALO", parse_mode='Markdown')
        return

    current_drivers_code = get_current_drivers_code()

    for argument in arguments:
        print(type(argument))
        if argument not in current_drivers_code:
            bot.reply_to(
                message, f"Sorry buddy. There is no driver code equals to {argument}", parse_mode='Markdown'
            )
            return

    next_race = Race.get_next_race()

    text = f"Your prediction was saved for {next_race.race_name}😎 \n" +\
           f"🥇{arguments[0]}  🥈{arguments[1]}  🥉{arguments[2]}"

    Prediction.set(username, chat_id, next_race.race_id, next_race.season, arguments[0], arguments[1], arguments[2])
    bot.reply_to(message, text, parse_mode='Markdown')