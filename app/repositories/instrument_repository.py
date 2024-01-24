from app.models.models import Instrument, db_session


class InstrumentRepository:
    def get_all(self):
        return db_session.query(Instrument).all()

    def get_by_id(self, instrument_id):
        return db_session.query(Instrument).get(instrument_id)

    def create(self, instrument):
        db_session.add(instrument)
        db_session.commit()

    def update(self, instrument):
        db_session.commit()

    def delete(self, instrument):
        db_session.delete(instrument)
        db_session.commit()
