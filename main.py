import os

from flask import Flask
from flask_cors import CORS

from app.controllers.category_controller import CategoryController
from app.controllers.customer_order_controller import CustomerOrderController
from app.controllers.instrument_controller import InstrumentController
from app.controllers.manufacturer_controller import ManufacturerController
from app.controllers.instrument_item_controller import InstrumentItemController
from app.models.models import seed_all_data
from app.repositories.category_repository import CategoryRepository
from app.repositories.customer_order_repository import CustomerOrderRepository
from app.repositories.instrument_item_repository import InstrumentItemRepository
from app.repositories.instrument_repository import InstrumentRepository
from app.repositories.manufacturer_repository import ManufacturerRepository
from app.services.category_service import CategoryService
from app.services.customer_order_service import CustomerOrderService
from app.services.instrument_item_service import InstrumentItemService
from app.services.instrument_service import InstrumentService
from app.services.manufacturer_service import ManufacturerService

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instruments.sqlite.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.sort_keys = False

instrument_repository = InstrumentRepository()
instrument_service = InstrumentService(instrument_repository)
instrument_controller = InstrumentController(instrument_service)

category_repository = CategoryRepository()
category_service = CategoryService(category_repository)
category_controller = CategoryController(category_service)


manufacturer_repository = ManufacturerRepository()
manufacturer_service = ManufacturerService(manufacturer_repository)
manufacturer_controller = ManufacturerController(
    manufacturer_service=manufacturer_service
)

instrument_item_repository = InstrumentItemRepository()
instrument_item_service = InstrumentItemService(instrument_item_repository)
instrument_item_controller = InstrumentItemController(instrument_item_service)

customer_order_repository = CustomerOrderRepository()
customer_order_service = CustomerOrderService(
    customer_order_repository, instrument_item_repository
)
customer_order_controller = CustomerOrderController(customer_order_service)


# # Define routes
# /instruments
app.add_url_rule(
    "/instruments",
    "get_all_instruments",
    instrument_controller.get_all_instruments,
    methods=["GET"],
)
app.add_url_rule(
    "/instruments/<int:instrument_id>",
    "get_instrument_by_id",
    instrument_controller.get_instrument_by_id,
    methods=["GET"],
)
app.add_url_rule(
    "/instruments",
    "create_instrument",
    instrument_controller.create_instrument,
    methods=["POST"],
)
app.add_url_rule(
    "/instruments/<int:instrument_id>",
    "update_instrument",
    instrument_controller.update_instrument,
    methods=["PUT"],
)
app.add_url_rule(
    "/instruments/<int:instrument_id>",
    "delete_instrument",
    instrument_controller.delete_instrument,
    methods=["DELETE"],
)

# /categories
app.add_url_rule(
    "/categories", "get_all_categories", category_controller.get_all, methods=["GET"]
)
app.add_url_rule(
    "/categories/<int:category_id>",
    "get_category_by_id",
    category_controller.get_by_id,
    methods=["GET"],
)

# /instrument_item
app.add_url_rule(
    "/instrument-items",
    "get_instrument_items",
    instrument_item_controller.get_all_instrument_item,
    methods=["GET"],
)
app.add_url_rule(
    "/instrument-items/<int:instrument_item_id>",
    "get_instrument_item_by_id",
    instrument_item_controller.get_instrument_item_by_id,
    methods=["GET"],
)
app.add_url_rule(
    "/instrument-items",
    "create_instrument_item",
    instrument_item_controller.create_instrument_item,
    methods=["POST"],
)
app.add_url_rule(
    "/instrument-items/<int:instrument_item_id>",
    "update_instrument_item",
    instrument_item_controller.update_instrument_item,
    methods=["PUT"],
)
# add url POST for delete /instrument_item/{instrument_item_id} that will calling controller of instrument item
app.add_url_rule(
    "/instrument-items/<int:instrument_item_id>",
    "delete_instrument_item",
    instrument_item_controller.delete_instrument_item,
    methods=["DELETE"],
)

# /customer_orders
app.add_url_rule(
    "/customer-orders",
    "get_all_customer_orders",
    customer_order_controller.get_all_customer_order,
    methods=["GET"],
)
app.add_url_rule(
    "/customer-orders",
    "create_customer_order",
    customer_order_controller.create_customer_order,
    methods=["POST"],
)
# add url PUT for update /instrument_item/{instrument_item_id} that will calling controller of instrument item


# /manufacturer
app.add_url_rule(
    "/manufacturers",
    "get_all_manufacturers",
    manufacturer_controller.get_all,
    methods=["GET"],
)
app.add_url_rule(
    "/manufacturers/<int:manufacturer_id>",
    "get_manufacturer_by_id",
    manufacturer_controller.get_by_id,
    methods=["GET"],
)


def is_first_run():
    return not os.path.exists("initialized.flag")


if __name__ == "__main__":
    if is_first_run():
        seed_all_data()
    app.run(debug=True, port=8080)
