from flask import jsonify

from app.services.category_service import CategoryService


class CategoryController:
    __category_service: CategoryService

    def __init__(self, category_service: CategoryService = None):
        self.__category_service = category_service or CategoryService()

    def get_all(self):
        try:
            categories = self.__category_service.get_all()
            response = [category.serialize() for category in categories]
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def get_by_id(self, category_id):
        try:
            category = self.__category_service.get_by_id(category_id)
            if category:
                return jsonify(category.serialize()), 200
            return jsonify({'error': 'Category not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
