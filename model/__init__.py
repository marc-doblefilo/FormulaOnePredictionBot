from application import db
from src.league.domain import league
from src.user.domain import user

# Last line
db.drop_all()
db.create_all()
