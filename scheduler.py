from datetime import datetime
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import UTC, timezone
import xmltodict
import requests
from src.race.application.closes_race import closes_race

from src.race.domain.race import Race

def test():
    print('Race is starting')

def schedule_next_race():
    next_race = Race.get_next_race()
    scheduler = BackgroundScheduler(timezone="UTC")

    response = requests.get(f'https://ergast.com/api/f1/current/{next_race.race_id}')

    doc = xmltodict.parse(response.text)

    race = doc['MRData']['RaceTable']['Race']
    date = datetime.strptime(race['Date'] + " " + race['Time'], '%Y-%m-%d %H:%M:%SZ')
    print(date)
    print(date.hour)

    trigger = CronTrigger(year=date.year, month=date.month, day=date.day, hour=date.hour, minute=date.minute, timezone="UTC")

    job = scheduler.add_job(closes_race, trigger=trigger)

    scheduler.start()
