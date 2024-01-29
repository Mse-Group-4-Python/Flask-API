from app.models.models import InstrumentItem, db_session


class InstrumentItemRepository:
    def get_all(self, **kwargs):
        query = db_session.query(InstrumentItem).join(InstrumentItem.instrument)
        for key, value in kwargs.items():
            query = query.filter_by(**{key: value})
        return query.all()

    def get_by_id(self, instrument_item_id):
        return db_session.query(InstrumentItem).get(instrument_item_id)

    def create(self, instrument_item):
        db_session.add(instrument_item)
        db_session.commit()

    def update(self, instrument_item_id, instrument_item):
        db_session.query(InstrumentItem).filter_by(id=instrument_item_id).update(
            instrument_item
        )
        db_session.commit()

    def delete(self, instrument_item_id):
        db_session.query(InstrumentItem).filter_by(id=instrument_item_id).delete()
        db_session.commit()
