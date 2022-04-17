from application.config import TOKEN, SECRET_TOKEN, HEROKU_APP_NAME, DATABASE_URL
from application.config import bot, app, db
from src.driver.application import \
    drivers_command
from src.league.application import standings_command, startleague_command
from src.user.application import leave_command, register_command, changepoints_command
from src.race.application import get_races
from application import help_command
