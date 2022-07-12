# coding=utf-8
from application.config import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Text, nullable=False)
    leagueId = db.Column(db.BigInteger, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    db.create_all()

    @staticmethod
    def set(userId, leagueId):
        record = db.session.query(User).filter_by(
            userId=userId, leagueId=leagueId).first()

        if record is None:
            record = User(userId=userId, leagueId=leagueId, points=0, isAdmin=False,
                          created_at=datetime.now())
            db.session.add(record)

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def set_new_user_as_admin(userId, leagueId):
        record = db.session.query(User).filter_by(
            userId=userId, leagueId=leagueId).first()

        if record is None:
            record = User(userId=userId, leagueId=leagueId, points=0, isAdmin=True,
                          created_at=datetime.now())
            db.session.add(record)

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def set_new_points(userId, leagueId, newPoints):
        record = db.session.query(User).filter_by(
            userId=userId, leagueId=leagueId).update({User.points: newPoints})

        db.session.commit()
        db.session.close()

        return record

    @staticmethod
    def add_points(userId, leagueId, points):
        record = db.session.query(User).filter_by(
            userId=userId, leagueId=leagueId).update({User.points: User.points + points})

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
    def remove_all_from_league(leagueId):
        record = db.session.query(User).filter_by(leagueId=leagueId).first()

        if record is not None:
            db.session.query(User).filter_by(leagueId=leagueId).delete()

        db.session.commit()
        db.session.close()

    @staticmethod
    def get_all_from_a_league(leagueId):
        record = db.session.query(User).filter_by(leagueId=leagueId).all()
        db.session.close()

        return record

    @staticmethod
    def get_all_from_a_league_order_by_points(leagueId):
        record = db.session.query(User).filter_by(leagueId=leagueId).all()
        db.session.close()

        record = sorted(record, key=lambda x: x.points, reverse=True)

        return record

    @staticmethod
    def is_admin(userId, leagueId):
        record = db.session.query(User).filter_by(
            leagueId=leagueId, userId=userId).first()
        db.session.close()

        if record.isAdmin:
            return True

        return False
