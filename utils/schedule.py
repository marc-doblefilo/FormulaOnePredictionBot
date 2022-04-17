from datetime import datetime, timedelta
from apscheduler.triggers.cron import CronTrigger
import xmltodict
import requests
from src.race.application.closes_race import closes_race
from src.race.application.finish_race import finish_race

from application import scheduler
from src.race.domain.race import Race

def test():
    print('Race is starting')

def schedule_next_race():
    next_race = Race.get_next_race()

    response = requests.get(f'https://ergast.com/api/f1/current/{next_race.race_id}')

    doc = xmltodict.parse(response.text)

    race = doc['MRData']['RaceTable']['Race']
    date = datetime.strptime(race['Date'] + " " + race['Time'], '%Y-%m-%d %H:%M:%SZ')

    trigger = CronTrigger(year=date.year, month=date.month, day=date.day, hour=date.hour, minute=date.minute, timezone="UTC")

    job = scheduler.add_job(closes_race, trigger=trigger)



def schedule_check_results_2_hours_after_race_starts():

    now = datetime.utcnow()
    schedule_date = now + timedelta(hours=2)
    trigger = CronTrigger(
        year=schedule_date.year, month=schedule_date.month, day=schedule_date.day,
        hour=schedule_date.hour, minute=schedule_date.minute, timezone="UTC")

    job = scheduler.add_job(finish_race, trigger=trigger)


def schedule_next_repeated_check_results_30_minutes_after_last_check():

    now = datetime.utcnow()
    schedule_date = now + timedelta(minutes=30)
    trigger = CronTrigger(
        year=schedule_date.year, month=schedule_date.month, day=schedule_date.day,
        hour=schedule_date.hour, minute=schedule_date.minute, timezone="UTC")

    job = scheduler.add_job(finish_race, trigger=trigger)
