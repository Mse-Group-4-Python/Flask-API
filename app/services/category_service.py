from typing import Optional

from app.models.category_model import CategoryModel
from app.repositories.category_repository import CategoryRepository


class CategoryService:
    __category_repository: CategoryRepository

    def __init__(self, _category_repository=None):
        self.__category_repository = _category_repository

    def get_all(self) -> list[CategoryModel]:
        return [
            CategoryModel(
                category_id=entity.id,
                category_name=entity.category_name,
            )
            for entity in self.__category_repository.get_all()
        ]

    def get_by_id(self, category_id) -> Optional[CategoryModel]:
        entity = self.__category_repository.get_by_id(category_id)
        return CategoryModel(entity.id, entity.category_name) if entity else None
