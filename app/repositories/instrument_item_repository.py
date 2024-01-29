from app.models.models import InstrumentItem, db_session


class InstrumentItemRepository:
    def get_all(self, **kwargs):
        query = db_session.query(InstrumentItem)
        if kwargs:
            if kwargs.get("instrument_id"):
                query = query.filter_by(instrument_id=kwargs.get("instrument_id"))
            if kwargs.get("serial_number"):
                query = query.filter_by(serial_number=kwargs.get("serial_number"))
            if kwargs.get("year_of_purchase"):
                query = query.filter_by(year_of_purchase=kwargs.get("year_of_purchase"))
            if kwargs.get("description"):
                query = query.filter(
                    InstrumentItem.description.like(f"%{kwargs.get('description')}%")
                )
            if kwargs.get("price"):
                query = query.filter_by(price=kwargs.get("price"))
            if kwargs.get("category_id", False) or kwargs.get("manufacturer_id", False):
                query = query.join(InstrumentItem.instrument)
                if kwargs.get("category_id"):
                    query = query.filter_by(
                        category_id=kwargs.get("category_id"),
                    )
                if kwargs.get("manufacturer_id"):
                    query = query.filter_by(
                        manufacturer_id=kwargs.get("manufacturer_id")
                    )

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
