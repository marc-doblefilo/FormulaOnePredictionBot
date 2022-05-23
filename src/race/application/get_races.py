# coding=utf-8
import logging
from application import bot
from src.race.domain.race import Race
from src.race.infrastructure.get_current_races import get_current_races


def get_races():
    total = Race.set()
    logging.info(f'A total of {total} new races were saved.')
