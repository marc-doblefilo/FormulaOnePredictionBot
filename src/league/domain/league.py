# coding=utf-8
from datetime import datetime
from application.config import db


class League(db.Model):
    __tablename__ = 'league'
    id = db.Column(db.Integer, primary_key=True)
    leagueId = db.Column(db.BigInteger, nullable=False)
    leagueName = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def set(id, leagueName):
        record = db.session.query(League).filter_by(leagueId=id).first()

        if record is None:
            record = League(leagueId=id, leagueName=leagueName,
                            created_at=datetime.now())
            db.session.add(record)

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def get(id):
        record = db.session.query(League).filter_by(leagueId=id).first()
        db.session.close()

        return record

    @staticmethod
    def get_all():
        record = db.session.query(League).filter_by().all()
        db.session.close()

        return record

    def remove(id):
        record = db.session.query(League).filter_by(leagueId=id).first()

        if record is not None:
            db.session.query(League).filter_by(leagueId=id).delete()

        db.session.commit()
        db.session.close()
