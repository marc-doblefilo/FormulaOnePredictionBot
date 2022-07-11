# coding=utf-8
import logging
import requests
import xmltodict

from application import bot
import utils.schedule as schedule
from src.race.domain.race import Race
from src.league.domain.league import League
from src.user.domain.user import User
from src.prediction.domain.prediction import Prediction

from utils.sum_points import sum_points


def finish_race():
    leagues = League.get_all()

    race = Race.get_current_race()

    response = requests.get(
        f'https://ergast.com/api/f1/current/{race.race_id}/results')

    doc = xmltodict.parse(response.text, process_namespaces=False)

    if(len(doc['MRData']['RaceTable']) == 2):
        schedule.schedule_next_repeated_check_results_30_minutes_after_last_check()
        return

    data = doc['MRData']['RaceTable']['Race']['ResultsList']

    results = [data['Result'][0]['Driver']['@code'], data['Result']
               [1]['Driver']['@code'], data['Result'][2]['Driver']['@code']]

    Race.finish(race.season, race.race_id)
    schedule.schedule_next_race()
    for league in leagues:
        predictions = Prediction.get_all_by_race(
            league.leagueId, race.race_id, race.season)
        for prediction in predictions:
            predict = [prediction.p1, prediction.p2, prediction.p3]
            User.add_points(prediction.user_id, league.leagueId,
                            sum_points(results, predict))

        try:
            bot.send_message(league.leagueId, f'CHECKERED FLAG🏁 Check /standings to see race results.',
                             parse_mode='Markdown')
        except:
            logging.error(
                f'Cannot send a message to this group: {league.leagueId}')
