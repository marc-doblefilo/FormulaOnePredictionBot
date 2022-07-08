import logging
import requests
import xmltodict
from datetime import datetime
import pytz

from src.race.domain.race import Race


def get_next_race_schedule():
    schedule = {}

    response = requests.get('https://ergast.com/api/f1/current/next')

    doc = xmltodict.parse(response.text)

    race = doc['MRData']['RaceTable']['Race']
    date = datetime.strptime(
        race['Date'] + " " + race['Time'], '%Y-%m-%d %H:%M:%SZ')

    date = pytz.utc.localize(date)

    schedule['Race'] = date

    try:
        date = datetime.strptime(
            race['FirstPractice']['Date'] + " " + race['FirstPractice']['Time'], '%Y-%m-%d %H:%M:%SZ')

        date = pytz.utc.localize(date)

        schedule['First Practice'] = date
    except:
        logging.debug('This race has no First Practice session')

    try:
        date = datetime.strptime(
            race['SecondPractice']['Date'] + " " + race['SecondPractice']['Time'], '%Y-%m-%d %H:%M:%SZ')

        date = pytz.utc.localize(date)

        schedule['Second Practice'] = date
    except:
        logging.debug('This race has no Second Practice session')

    try:
        date = datetime.strptime(
            race['ThirdPractice']['Date'] + " " + race['ThirdPractice']['Time'], '%Y-%m-%d %H:%M:%SZ')

        date = pytz.utc.localize(date)

        schedule['Third Practice'] = date
    except:
        logging.debug('This race has no Third Practice session')

    try:
        date = datetime.strptime(
            race['Sprint']['Date'] + " " + race['Sprint']['Time'], '%Y-%m-%d %H:%M:%SZ')

        date = pytz.utc.localize(date)

        schedule['Sprint'] = date
    except:
        logging.debug('This race has no Sprint session')

    try:
        date = datetime.strptime(
            race['Qualifying']['Date'] + " " + race['Qualifying']['Time'], '%Y-%m-%d %H:%M:%SZ')

        date = pytz.utc.localize(date)

        schedule['Qualifying'] = date
    except:
        logging.debug('This race has no Qualifying session')

    return schedule
