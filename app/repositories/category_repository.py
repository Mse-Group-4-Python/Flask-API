from sqlalchemy.orm import Session

from app.models.models import Category, db_session


class CategoryRepository:
    __db_session: Session = None

    def __init__(self, _db_session=None):
        self.__db_session = _db_session or db_session

    def get_all(self) -> list[Category]:
        return self.__db_session.query(Category).all()

    def get_by_id(self, category_id):
        return self.__db_session.query(Category).get(category_id)

    def create(self, category):
        return self.__db_session.add(category)

    def update(self, category_id, category):
        return (
            self.__db_session.query(Category).filter_by(id=category_id).update(category)
        )

    def delete(self, category_id):
        return self.__db_session.query(Category).filter_by(id=category_id).delete()
