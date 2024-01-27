from app.models.models import InstrumentItem, db_session


class InstrumentItemRepository:
    def get_all(self):
        return db_session.query(InstrumentItem).all()

    def get_by_id(self, instrument_item_id):
        return db_session.query(InstrumentItem).get(instrument_item_id)

    def create(self, instrument_item):
        db_session.add(instrument_item)
        db_session.commit()