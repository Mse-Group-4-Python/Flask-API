from app.models.models import Instrument, db_session
from sqlalchemy.orm import noload

class InstrumentRepository:
    def get_all(self):
        return db_session.query(Instrument).all()

    def get_by_id(self, instrument_id):
        return db_session.query(Instrument).get(instrument_id)

    def create(self, instrument):
        db_session.add(instrument)
        db_session.commit()

    def update(self, instrument):
        update_values = {
        'instrument_name': instrument.instrument_name,
        'manufacturer_id': instrument.manufacturer_id,
        'category_id': instrument.category_id,
        'description': instrument.description,
        'color': instrument.color,
        'tags': instrument.tags,
        'id' : instrument.id[0]
    }
        db_session.query(Instrument).filter_by(id=instrument.id[0]).update(update_values)
        db_session.commit()

    def delete(self, instrument):
        db_session.delete(instrument)
        db_session.commit()
