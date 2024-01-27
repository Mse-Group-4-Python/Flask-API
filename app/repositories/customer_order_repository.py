from flask_sqlalchemy.session import Session

from app.models.models import CustomerOrder, db_session


class CustomerOrderRepository:
    __db_session: Session = None

    def __init__(self, _db_session=None):
        self.__db_session = _db_session or db_session

    def get_all(self):
        return self.__db_session.query(CustomerOrder).all()

    def create(self, customer_order: CustomerOrder):
        self.__db_session.add(customer_order)
        self.__db_session.commit()
