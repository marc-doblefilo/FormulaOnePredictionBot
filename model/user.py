# coding=utf-8
from datetime import datetime
from model import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Text, nullable=False)
    leagueId = db.Column(db.BigInteger, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def set(userId, leagueId):
        record = db.session.query(User).filter_by(
            userId=userId, leagueId=leagueId).first()

        if record is None:
            record = User(userId=userId, leagueId=leagueId, points=0,
                          created_at=datetime.now())
            db.session.add(record)

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def get(userId, leagueId):
        record = db.session.query(User).filter_by(
            userId=userId, leagueId=leagueId).first()
        db.session.close()

        return record

    @staticmethod
    def remove(userId, leagueId):
        record = db.session.query(User).filter_by(
            userId=userId, leagueId=leagueId).first()

        if record is not None:
            db.session.query(User).filter_by(
                userId=userId, leagueId=leagueId).delete()

        db.session.commit()
        db.session.close()

    @staticmethod
    def get_all_from_a_league(leagueId):
        record = db.session.query(User).filter_by(leagueId=leagueId).all()
        db.session.close()

        return record
