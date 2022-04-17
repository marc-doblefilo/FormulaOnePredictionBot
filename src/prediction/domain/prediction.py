# coding=utf-8
from datetime import datetime
from model import db
from src.race.infrastructure.get_current_races import get_current_races


class Prediction(db.Model):
    __tablename__ = 'prediction'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Text, nullable=False)
    league_id = db.Column(db.BigInteger, nullable=False)
    race_id = db.Column(db.Text, nullable=False)
    race_season = db.Column(db.Text, nullable=False)
    p1 = db.Column(db.Text, nullable=False)
    p2 = db.Column(db.Text, nullable=False)
    p3 = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def set(user_id, league_id, race_id, race_season, p1: str, p2: str, p3: str):
        record = db.session.query(Prediction).filter_by(user_id=user_id, league_id=league_id, race_id=race_id, race_season=race_season).first()

        if record is None:
            record = Prediction(user_id=user_id, league_id=league_id,
            race_id=race_id, race_season=race_season,
            p1=p1, p2=p2, p3=p3, created_at=datetime.now())
            db.session.add(record)

        if record is not None:
            record = db.session.query(Prediction).filter_by(user_id=user_id, league_id=league_id, race_id=race_id, race_season=race_season).update({
                Prediction.p1: p1,
                Prediction.p2: p2,
                Prediction.p3: p3
            })

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def get_all_by_race(league_id, race_id, race_season) -> list:
        record = db.session.query(Prediction).filter_by(
            league_id=league_id,
            race_id=race_id,
            race_season=race_season
        ).all()
        db.session.close()

        return record