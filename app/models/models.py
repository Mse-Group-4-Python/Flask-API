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

def add_category_data():
    category_1 = Category(id=1, category_name="Guitar")
    category_2 = Category(id=2, category_name="Drums")
    category_3 = Category(id=3, category_name="Xylophone")
    category_4 = Category(id=4, category_name="Cymbals")
    category_5 = Category(id=5, category_name="Bayan")
    category_6 = Category(id=6, category_name="Tom-tom")                    
    category_7 = Category(id=7, category_name="Conga")
    category_8 = Category(id=8, category_name="Bell")
    category_9 = Category(id=9, category_name="Mridangam")
    category_10 = Category(id=10, category_name="Whistle")
    category_11 = Category(id=11, category_name="Accordion")
    category_12 = Category(id=12, category_name="Organ")
    category_13 = Category(id=13, category_name="Trumpet")
    category_14 = Category(id=14, category_name="Clarinet")
    category_15 = Category(id=15, category_name="Bagpipe")
    category_16 = Category(id=16, category_name="Sirens")
    category_17 = Category(id=17, category_name="Trombone")
    category_18 = Category(id=18, category_name="Recorder")
    category_19 = Category(id=19, category_name="Harmonica")
    category_20 = Category(id=20, category_name="Tumpong")
    db_session.add_all([category_1, category_2,category_3,category_4,category_5,category_6,category_7
                        ,category_8,category_9,category_10,category_11, category_12, category_13, category_14, category_15, category_16,
                        category_17, category_18, category_19, category_20])
    db_session.commit()

def add_manufacturer_data():
    manufacturer_1 = Manufacturer(id=1, manufacturer_name="Yamaha")
    manufacturer_2 = Manufacturer(id=2, manufacturer_name="Kawai")
    manufacturer_3 = Manufacturer(id=3, manufacturer_name="Gibson")
    manufacturer_4 = Manufacturer(id=4, manufacturer_name="Harman Professional")
    manufacturer_5 = Manufacturer(id=5, manufacturer_name="Shure")
    manufacturer_6 = Manufacturer(id=6, manufacturer_name="Fender Musical Instruments")
    manufacturer_7 = Manufacturer(id=7, manufacturer_name="Steinway Musical Instruments")
    manufacturer_8 = Manufacturer(id=8, manufacturer_name="Sennheiser")
    manufacturer_9 = Manufacturer(id=9, manufacturer_name="Roland")
    manufacturer_10 = Manufacturer(id=10, manufacturer_name="C. F. Martin and Company")
    manufacturer_11= Manufacturer(id=11, manufacturer_name="GUANG DONG SHENG KAI MUSICAL INSTRU")
    db_session.add_all([manufacturer_1, manufacturer_2,manufacturer_3,manufacturer_4,manufacturer_5,
                        manufacturer_6,manufacturer_7,manufacturer_8,manufacturer_9,manufacturer_10,manufacturer_11])
    db_session.commit()


def seed_all_data():
    add_category_data()
    add_manufacturer_data()
    
    with open("initialized.flag", "w") as flag_file:
        flag_file.write("initialized")
