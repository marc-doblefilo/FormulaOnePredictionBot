# coding=utf-8
from application import bot
from src.prediction.domain.prediction import Prediction
from src.race.domain.race import Race
from src.league.domain.league import League
from src.user.domain.user import User
from utils.tables import create_predictions_table


@bot.message_handler(commands=['predictions'])
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

    race = None
    if Race.get_current_race() is None:
        race = Race.get_next_race()
    elif Race.get_current_race() is not None:
        race = Race.get_current_race()

    predictions = Prediction.get_all_by_race(chat_id, race.race_id, race.season)

    table = create_predictions_table(predictions)

    bot.send_message(chat_id, f'<b>{race.race_name}</b>\n<pre>{table}</pre>',
                parse_mode='HTML')