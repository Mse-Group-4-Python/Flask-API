from app.models.models import Instrument  
from app import db

class InstrumentRepository:
    def get_all(self):
        return db.session.query(Instrument).all()

    def get_by_id(self, instrument_id):
        return db.session.query(Instrument).get(instrument_id)

    def create(self, instrument):
        db.session.add(instrument)
        db.session.commit()

    def update(self, instrument):
        db.session.commit()

    def delete(self, instrument):
        db.session.delete(instrument)
        db.session.commit()
