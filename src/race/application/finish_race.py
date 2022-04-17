# coding=utf-8
import logging
import requests
import xmltodict
from datetime import datetime

from application import bot
import utils.schedule as schedule
from src.race.domain.race import Race
from src.league.domain.league import League

def finish_race():
    leagues = League.get_all()

    race = Race.get_current_race()

    response = requests.get(f'https://ergast.com/api/f1/current/{race.race_id}/results')

    doc = xmltodict.parse(response.text)

    if(len(doc['MRData']['RaceTable']) == 2):
        schedule.schedule_next_repeated_check_results_30_minutes_after_last_check()
        return

    Race.finish(race.season, race.race_id)
    schedule.schedule_next_race()
    for league in leagues:
        bot.send_message(league.leagueId, f'CHECKERED FLAG🏁 Here we have the results.',
                parse_mode='Markdown')
