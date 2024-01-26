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

    def create(self, category):
        try:
            self.__category_service.create(category)
            return jsonify({'message': 'Category created successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def update(self, category_id, category):
        try:
            self.__category_service.update(category_id, category)
            return jsonify({'message': 'Category updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    def delete(self, category_id):
        try:
            self.__category_service.delete(category_id)
            return jsonify({'message': 'Category deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
