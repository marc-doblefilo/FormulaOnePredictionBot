# coding=utf-8
from datetime import datetime
from model import db
from src.race.infrastructure.get_current_races import get_current_races


class Race(db.Model):
    __tablename__ = 'race'
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Text, nullable=False)
    race_id = db.Column(db.Text, nullable=False)
    race_name = db.Column(db.Text, nullable=False)
    is_closed = db.Column(db.Boolean, nullable=False)
    is_finished = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def set():
        races = get_current_races()
        new_races_saved = 0
        
        if races == None or races == 0:
            return

        for race in races:
            record = db.session.query(Race).filter_by(season=race[0], race_id=race[1], race_name=race[2]).first()

            if record is None:
                record = Race(season=race[0], race_id=race[1], race_name=race[2], is_closed=race[3], is_finished=race[4], created_at=datetime.now())
                db.session.add(record)
                new_races_saved += 1
            if record is not None and record.is_closed != race[3] or record.is_finished != race[4]:
                db.session.query(Race).filter_by(season=race[0], race_id=race[1], race_name=race[2]).delete()
                record = Race(season=race[0], race_id=race[1], race_name=race[2], is_closed=race[3], is_finished=race[4], created_at=datetime.now())
                db.session.add(record)
                new_races_saved += 1
            
        db.session.commit()
        db.session.close()

        return new_races_saved

    @staticmethod
    def closes_a_race(season_id, race_id):
        record = db.session.query(Race).filter_by(season=season_id, race_id=race_id).first()

        if record is not None:
            record = db.session.query(Race).filter_by(season=season_id, race_id=race_id).update({Race.is_closed: True})

        db.session.commit()
        db.session.close()
        
        return record

    @staticmethod
    def finish(season_id, race_id):
        record = db.session.query(Race).filter_by(season=season_id, race_id=race_id).first()

        if record is not None:
            record = db.session.query(Race).filter_by(season=season_id, race_id=race_id).update({Race.is_finished: True})

        db.session.commit()
        db.session.close()
        
        return record

    @staticmethod
    def get():
        record = db.session.query(Race).filter_by().all()
        db.session.close()

        return record
    
    def get_next_race():
        record = db.session.query(Race).filter_by(is_closed=False, is_finished=False).all()
        db.session.close()

        record = sorted(record, key=lambda x: int(x.race_id), reverse=False)

        return record[0]

    def get_current_race():
        record = db.session.query(Race).filter_by(is_closed=True, is_finished=False).all()
        db.session.close()

        record = sorted(record, key=lambda x: int(x.race_id), reverse=False)

        if len(record) == 0:
            return None
        
        return record[0]