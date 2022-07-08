from application.config import TOKEN, SECRET_TOKEN, HEROKU_APP_NAME, DATABASE_URL
from application.config import bot, app, db, scheduler
from src.driver.application import \
    drivers
from src.league.application import removeleague, standings, startleague
from src.user.application import register, changepoints, leave
from src.race.application import get_races, next_race
from application import help_command
from src.prediction.application import predict, predictions
