# coding=utf-8
from ast import arg
import requests
import xmltodict

from application import bot
from utils.extract_arguments import extract_arguments_without_command
import utils.schedule as schedule
from src.race.domain.race import Race
from src.league.domain.league import League
from src.user.domain.user import User
from src.prediction.domain.prediction import Prediction

from utils.sum_points import sum_points

@bot.message_handler(commands=['checkresults'])
def finish_race(message):

    chat_id = message.chat.id
    username = message.from_user.username

    if chat_id > 0:
        bot.reply_to(
            message, "This is not a group. Please use me only in groups 😔", parse_mode='Markdown')
        return

    if League.get(chat_id) == None:
        bot.reply_to(
            message, "There is no league in this group. Use /startleague to start one! 😎", parse_mode='Markdown')
        return

    if User.is_admin(username, chat_id) == False:
        bot.reply_to(
            message, "Sorry you are not the admin of this league. 😬", parse_mode='Markdown')
        return

    arguments = extract_arguments_without_command(message.text)

    race_id = arguments[0]
    race_season = arguments[1]

    response = requests.get(f'https://ergast.com/api/f1/current/{race_id}/results')

    doc = xmltodict.parse(response.text)

    if(len(doc['MRData']['RaceTable']) == 2):
        bot.reply_to(message, f"Sorry buddy, the race is not finished yet or I can not get the results", 
                parse_mode='Markdown')
        return

    data = doc['MRData']['RaceTable']['Race']['ResultsList']

    results = [ data['Result'][0]['Driver']['@code'], data['Result'][1]['Driver']['@code'], data['Result'][2]['Driver']['@code']]
    
    predictions = Prediction.get_all_by_race(chat_id, race_id, race_season)
    for prediction in predictions:
        predict = [prediction.p1, prediction.p2, prediction.p3]
        User.add_points(prediction.user_id, chat_id, sum_points(results, predict))
            
    bot.send_message(chat_id, f'CHECKERED FLAG🏁 Check /standings to see race results.',
            parse_mode='Markdown')
