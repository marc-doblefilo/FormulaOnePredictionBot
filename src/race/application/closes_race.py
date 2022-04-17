# coding=utf-8
from application import bot
import utils.schedule as schedule
from src.race.domain.race import Race
from src.league.domain.league import League

def closes_race():
    leagues = League.get_all()

    race = Race.get_next_race()

    Race.closes_a_race(race.season, race.race_id)

    schedule.schedule_check_results_2_hours_after_race_starts()

    for league in leagues:
        bot.send_message(league.leagueId, f'LIGHTS OUT AND AWAY WE GO! 🏁 Predictions are closed!',
                parse_mode='Markdown')
