import os
from flask import Flask
from app.models.models import seed_all_data
from app.controllers.instrument_controller import InstrumentController
from app.repositories.instrument_repository import InstrumentRepository
from app.services.instrument_service import InstrumentService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///instruments.sqlite.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

instrument_repository = InstrumentRepository()
instrument_service = InstrumentService(instrument_repository)
instrument_controller = InstrumentController(instrument_service)


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

def is_first_run():
    return not os.path.exists("initialized.flag")

if __name__ == '__main__':
    if is_first_run():
        seed_all_data()
    app.run(debug=True)
