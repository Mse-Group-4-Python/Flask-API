import os

from flask import Flask

from app.controllers.category_controller import CategoryController
from app.controllers.instrument_controller import InstrumentController
from app.controllers.manufacturer_controller import ManufacturerController
from app.models.models import seed_all_data
from app.repositories.category_repository import CategoryRepository
from app.repositories.instrument_repository import InstrumentRepository
from app.repositories.manufacturer_repository import ManufacturerRepository
from app.services.category_service import CategoryService
from app.services.instrument_service import InstrumentService
from app.services.manufacturer_service import ManufacturerService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///instruments.sqlite.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

instrument_repository = InstrumentRepository()
instrument_service = InstrumentService(instrument_repository)
instrument_controller = InstrumentController(instrument_service)

category_repository = CategoryRepository()
category_service = CategoryService(category_repository)
category_controller = CategoryController(category_service)

manufacturer_repository = ManufacturerRepository()
manufacturer_service = ManufacturerService(manufacturer_repository)
manufacturer_controller = ManufacturerController(manufacturer_service=manufacturer_service)



# # Define routes
# /instruments
app.add_url_rule('/instruments', 'get_all_instruments', instrument_controller.get_all_instruments, methods=['GET'])
app.add_url_rule('/instruments/<int:instrument_id>', 'get_instrument_by_id', instrument_controller.get_instrument_by_id,
                 methods=['GET'])
app.add_url_rule('/instruments', 'create_instrument', instrument_controller.create_instrument, methods=['POST'])
app.add_url_rule('/instruments/<int:instrument_id>', 'update_instrument', instrument_controller.update_instrument,
                 methods=['PUT'])
app.add_url_rule('/instruments/<int:instrument_id>', 'delete_instrument', instrument_controller.delete_instrument,
                 methods=['DELETE'])

# /categories
app.add_url_rule('/categories', 'get_all_categories', category_controller.get_all, methods=['GET'])
app.add_url_rule('/categories/<int:category_id>', 'get_category_by_id', category_controller.get_by_id,
                 methods=['GET'])


# /manufacturer
app.add_url_rule('/manufacturers', 'get_all_manufacturers', manufacturer_controller.get_all, methods=['GET'])
app.add_url_rule('/manufacturers/<int:manufacturer_id>', 'get_manufacturer_by_id', manufacturer_controller.get_by_id, methods=['GET'])


def is_first_run():
    return not os.path.exists("initialized.flag")


if __name__ == '__main__':
    if is_first_run():
        seed_all_data()
    app.run(debug=True)
