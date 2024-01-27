from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Double,
    ForeignKey, create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    relationship, sessionmaker, registry,
)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy model classes."""

    pass


class Category(Base):
    def __init__(self, id, category_name):
        super().__init__()
        self.category_name = category_name
        self.id = id

    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(255), nullable=False)
    instruments = relationship(
        "Instrument", back_populates="category"
    )


class Manufacturer(Base):

    def __init__(self, id, manufacturer_name):
        super().__init__()
        self.id = id
        self.manufacturer_name = manufacturer_name

    __tablename__ = "manufacturer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name = Column(String(255), nullable=False)
    instruments = relationship(
        "Instrument", back_populates="manufacturer"
    )


class Instrument(Base):
    __tablename__ = "instrument"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_name = Column(String(255), nullable=False)
    manufacturer_id = mapped_column(
        ForeignKey("manufacturer.id")
    )
    manufacturer = relationship(
        "Manufacturer", back_populates="instruments"
    )
    category_id = mapped_column(ForeignKey("category.id"))
    category = relationship(
        "Category", back_populates="instruments"
    )
    description = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    instrument_items = relationship(
        "InstrumentItem", back_populates="instrument"
    )
    tags = Column(String(255), nullable=False)

class InstrumentItem(Base):
    __tablename__ = "instrument_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_id = mapped_column(ForeignKey("instrument.id"))
    instrument = relationship(
        "Instrument", back_populates="instrument_items"
    )
    serial_number = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    year_of_purchase = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)
    order_items = relationship(
        "OrderItem", back_populates="instrument_item"
    )


class OrderItem(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_item_id = mapped_column(ForeignKey("instrument_item.id"))
    instrument_item = relationship("InstrumentItem", back_populates="order_items")
    quantity = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)
    customer_order_id = mapped_column(ForeignKey("customer_order.id"))
    customer_order = relationship(
        "CustomerOrder", back_populates="order_items"
    )


class CustomerOrder(Base):
    __tablename__ = "customer_order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255), nullable=False)
    delivery_address = Column(String(255), nullable=True)
    phone_number = Column(String(255), nullable=False)
    order_time = Column(DateTime, nullable=False)
    order_items = relationship(
        "OrderItem", back_populates="customer_order"
    )
    total_price = Column(Double, nullable=False)


engine = create_engine("sqlite:///instruments.sqlite.db", echo=True)
Base.metadata.create_all(engine)
metadata = Base.metadata
db_session = sessionmaker(bind=engine)()
mapper_registry = registry(metadata=metadata)
mapper_registry.configure()


# Path: entities/db_context.py


def seed_all_data():
    category_1 = Category(id=1, category_name="Guitar")
    category_2 = Category(id=2, category_name="Drums")
    db_session.add_all([category_1, category_2])
    db_session.commit()
    manufacturer_1 = Manufacturer(id=1, manufacturer_name="Yamaha")
    manufacturer_2 = Manufacturer(id=2, manufacturer_name="Kawai")
    db_session.add_all([manufacturer_1, manufacturer_2])
    db_session.commit()
    with open("initialized.flag", "w") as flag_file:
        flag_file.write("initialized")
