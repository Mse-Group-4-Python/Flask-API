from app.models.models import Manufacturer, db_session
from sqlalchemy.orm import Session

class ManufacturerRepository:

    __db_session: Session = None

    def __init__(self, _db_session=None):
        self.__db_session = _db_session or db_session


    def get_all(self):
        return self.__db_session.query(Manufacturer).all()
    
    def get_by_id(self, manufacturer_id):
        return self.__db_session.query(Manufacturer).get(manufacturer_id)
    
    