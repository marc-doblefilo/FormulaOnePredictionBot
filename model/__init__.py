from application import db
from src.league.domain import league
from src.user.domain import user
from src.race.domain import race
from src.prediction.domain import prediction

# Last line
db.create_all()
