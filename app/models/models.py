from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Double,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    mapped_column,
    relationship,
    sessionmaker,
    registry,
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
    instruments = relationship("Instrument", back_populates="category")


class Manufacturer(Base):
    def __init__(self, id, manufacturer_name):
        super().__init__()
        self.id = id
        self.manufacturer_name = manufacturer_name

    __tablename__ = "manufacturer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name = Column(String(255), nullable=False)
    instruments = relationship("Instrument", back_populates="manufacturer")


class Instrument(Base):
    __tablename__ = "instrument"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_name = Column(String(255), nullable=False)
    manufacturer_id = mapped_column(ForeignKey("manufacturer.id"))
    manufacturer = relationship("Manufacturer", back_populates="instruments")
    category_id = mapped_column(ForeignKey("category.id"))
    category = relationship("Category", back_populates="instruments")
    description = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    instrument_items = relationship("InstrumentItem", back_populates="instrument")
    tags = Column(String(255), nullable=False)


class InstrumentItem(Base):
    __tablename__ = "instrument_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_id = mapped_column(ForeignKey("instrument.id"))
    instrument = relationship("Instrument", back_populates="instrument_items")
    serial_number = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    year_of_purchase = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)
    order_items = relationship("OrderItem", back_populates="instrument_item")


class OrderItem(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_item_id = mapped_column(ForeignKey("instrument_item.id"))
    instrument_item = relationship("InstrumentItem", back_populates="order_items")
    quantity = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)
    customer_order_id = mapped_column(ForeignKey("customer_order.id"))
    customer_order = relationship("CustomerOrder", back_populates="order_items")


class CustomerOrder(Base):
    __tablename__ = "customer_order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255), nullable=False)
    delivery_address = Column(String(255), nullable=True)
    phone_number = Column(String(255), nullable=False)
    order_time = Column(DateTime, nullable=False)
    order_items = relationship("OrderItem", back_populates="customer_order")
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
    db_session.add_all(
        [
            category_1,
            category_2,
            category_3,
            category_4,
            category_5,
            category_6,
            category_7,
            category_8,
            category_9,
            category_10,
            category_11,
            category_12,
            category_13,
            category_14,
            category_15,
            category_16,
            category_17,
            category_18,
            category_19,
            category_20,
        ]
    )
    db_session.commit()


def add_manufacturer_data():
    manufacturer_1 = Manufacturer(id=1, manufacturer_name="Yamaha")
    manufacturer_2 = Manufacturer(id=2, manufacturer_name="Kawai")
    manufacturer_3 = Manufacturer(id=3, manufacturer_name="Gibson")
    manufacturer_4 = Manufacturer(id=4, manufacturer_name="Harman Professional")
    manufacturer_5 = Manufacturer(id=5, manufacturer_name="Shure")
    manufacturer_6 = Manufacturer(id=6, manufacturer_name="Fender Musical Instruments")
    manufacturer_7 = Manufacturer(
        id=7, manufacturer_name="Steinway Musical Instruments"
    )
    manufacturer_8 = Manufacturer(id=8, manufacturer_name="Sennheiser")
    manufacturer_9 = Manufacturer(id=9, manufacturer_name="Roland")
    manufacturer_10 = Manufacturer(id=10, manufacturer_name="C. F. Martin and Company")
    manufacturer_11 = Manufacturer(
        id=11, manufacturer_name="GUANG DONG SHENG KAI MUSICAL INSTRU"
    )
    db_session.add_all(
        [
            manufacturer_1,
            manufacturer_2,
            manufacturer_3,
            manufacturer_4,
            manufacturer_5,
            manufacturer_6,
            manufacturer_7,
            manufacturer_8,
            manufacturer_9,
            manufacturer_10,
            manufacturer_11,
        ]
    )
    db_session.commit()


def add_instrument():
    instrument_1 = Instrument(
        id=1,
        instrument_name="Alfaia",
        manufacturer_id=5,
        category_id=2,
        description="The alfaia is a Brazilian membranophone. It is a wooden drum made of animal skin tensioned or loosened through ropes placed alongside the body of the instrument.",
        color="Natural trumpets",
        tags="Membranophones",
    )
    instrument_2 = Instrument(
        id=2,
        instrument_name="Marimba",
        manufacturer_id=2,
        category_id=3,
        description="The marimba (/mərimbə/) is a musical instrument in the percussion family that consists of wooden bars that are struck by mallets",
        color="Wood",
        tags="Aerophones",
    )
    instrument_3 = Instrument(
        id=3,
        instrument_name="Kulintang",
        manufacturer_id=5,
        category_id=3,
        description="The ashiko is a drum, shaped like a tapered cylinder (or truncated cone) with the head on the wide end, and the narrow end open.",
        color="Black",
        tags="Idiophones",
    )
    instrument_4 = Instrument(
        id=4,
        instrument_name="Shekere",
        manufacturer_id=3,
        category_id=20,
        description="It is made of hardwood and generally has a calfskin hide. Nowadays, goatskin is sometimes used, in imitation of the high sound of the popular djembe drum.",
        color="Natural trumpets",
        tags="Membranophones",
    )
    instrument_5 = Instrument(
        id=5,
        instrument_name="Steelpan",
        manufacturer_id=5,
        category_id=4,
        description="The steelpan (also known as a pan, steel drum, and sometimes, collectively with other musicians, as a steelband or steel orchestra) is a musical instrument originating in Trinidad and Tobago. Steelpan musicians are called pannists.",
        color="Black",
        tags="Aerophones",
    )
    instrument_6 = Instrument(
        id=6,
        instrument_name="Tambourine",
        manufacturer_id=4,
        category_id=4,
        description="The tambourine is a musical instrument in the percussion family consisting of a frame, often of wood or plastic, with pairs of small metal jingles, called 'zills'.",
        color="Red",
        tags="Idiophones",
    )
    instrument_7 = Instrument(
        id=7,
        instrument_name="Triangle",
        manufacturer_id=2,
        category_id=4,
        description="The triangle is a musical instrument in the percussion family, and is classified as an idiophone in the Hornbostel-Sachs classification system. Triangles are made from a variety of metals including aluminum, beryllium copper, brass, bronze, iron, and steel. ",
        color="Silver",
        tags="Idiophones",
    )
    instrument_8 = Instrument(
        id=8,
        instrument_name="Vibraphone",
        manufacturer_id=6,
        category_id=3,
        description="Traditionally strapped over the shoulder, alfaias are played with a distinctive technique in which players hold the weak-hand drum stick inverted to get the proper attack on the head. ",
        color="White",
        tags="Idiophones",
    )
    instrument_9 = Instrument(
        id=9,
        instrument_name="Vibraslap",
        manufacturer_id=1,
        category_id=4,
        description="Vibraslap has a characteristic deep, heavy sound, different from other bass drums such as the surdo or kick-drum",
        color="Wood",
        tags="Membranophones",
    )
    instrument_10 = Instrument(
        id=10,
        instrument_name="Wooden fish",
        manufacturer_id=2,
        category_id=20,
        description="A wooden fish, also known as a Chinese temple block, wooden bell, or muyu, is a type of woodblock that originated from East Asia that is used by monks and lay people in the Mahayana tradition of Buddhism.",
        color="Natural",
        tags="Idiophones",
    )
    instrument_11 = Instrument(
        id=11,
        instrument_name="Bamboula",
        manufacturer_id=3,
        category_id=2,
        description="A bamboula is a type of drum made from a rum barrel with skin stretched over one end.It is also a dance accompanied by music from these drums.",
        color="Brown",
        tags="Membranophones",
    )
    instrument_12 = Instrument(
        id=14,
        instrument_name="Faia",
        manufacturer_id=7,
        category_id=2,
        description="The alfaia is a Brazilian membranophone. It is a wooden drum made of animal skin tensioned or loosened through ropes placed alongside the body of the instrument.",
        color="Natural trumpets",
        tags="Membranophones",
    )
    instrument_13 = Instrument(
        id=12,
        instrument_name="Mari",
        manufacturer_id=7,
        category_id=1,
        description="The marimba (/mərimbə/) is a musical instrument in the percussion family that consists of wooden bars that are struck by mallets",
        color="Wood",
        tags="Aerophones",
    )
    instrument_14 = Instrument(
        id=13,
        instrument_name="Lintang",
        manufacturer_id=7,
        category_id=3,
        description="The ashiko is a drum, shaped like a tapered cylinder (or truncated cone) with the head on the wide end, and the narrow end open.",
        color="Black",
        tags="Idiophones",
    )
    instrument_15 = Instrument(
        id=15,
        instrument_name="Steelpanne",
        manufacturer_id=7,
        category_id=4,
        description="The steelpan (also known as a pan, steel drum, and sometimes, collectively with other musicians, as a steelband or steel orchestra) is a musical instrument originating in Trinidad and Tobago. Steelpan musicians are called pannists.",
        color="Black",
        tags="Aerophones",
    )
    instrument_16 = Instrument(
        id=16,
        instrument_name="Ambourine",
        manufacturer_id=8,
        category_id=3,
        description="The tambourine is a musical instrument in the percussion family consisting of a frame, often of wood or plastic, with pairs of small metal jingles, called 'zills'.",
        color="Red",
        tags="Idiophones",
    )
    instrument_17 = Instrument(
        id=17,
        instrument_name="Fourangle",
        manufacturer_id=8,
        category_id=4,
        description="The triangle is a musical instrument in the percussion family, and is classified as an idiophone in the Hornbostel-Sachs classification system. Triangles are made from a variety of metals including aluminum, beryllium copper, brass, bronze, iron, and steel. ",
        color="Silver",
        tags="Idiophones",
    )
    instrument_18 = Instrument(
        id=18,
        instrument_name="Theaphone",
        manufacturer_id=9,
        category_id=4,
        description="Traditionally strapped over the shoulder, alfaias are played with a distinctive technique in which players hold the weak-hand drum stick inverted to get the proper attack on the head. ",
        color="White",
        tags="Idiophones",
    )
    instrument_19 = Instrument(
        id=19,
        instrument_name="Guaslap",
        manufacturer_id=10,
        category_id=10,
        description="Vibraslap has a characteristic deep, heavy sound, different from other bass drums such as the surdo or kick-drum",
        color="Wood",
        tags="Membranophones",
    )
    instrument_20 = Instrument(
        id=20,
        instrument_name="IshWooden",
        manufacturer_id=11,
        category_id=4,
        description="A wooden fish, also known as a Chinese temple block, wooden bell, or muyu, is a type of woodblock that originated from East Asia that is used by monks and lay people in the Mahayana tradition of Buddhism.",
        color="Natural",
        tags="Idiophones",
    )
    instrument_21 = Instrument(
        id=21,
        instrument_name="Bamboohi",
        manufacturer_id=1,
        category_id=3,
        description="A bamboula is a type of drum made from a rum barrel with skin stretched over one end.It is also a dance accompanied by music from these drums.",
        color="Brown",
        tags="Membranophones",
    )

    db_session.add_all(
        [
            instrument_1,
            instrument_2,
            instrument_3,
            instrument_4,
            instrument_5,
            instrument_6,
            instrument_7,
            instrument_8,
            instrument_9,
            instrument_10,
            instrument_11,
            instrument_12,
            instrument_13,
            instrument_14,
            instrument_15,
            instrument_16,
            instrument_17,
            instrument_18,
            instrument_19,
            instrument_20,
            instrument_21,
        ]
    )
    db_session.commit()


def add_instrucment_item():
    instrument_item_1 = InstrumentItem(
        id=1,
        instrument_id=1,
        serial_number="211.211.2",
        description="Cambodia",
        year_of_purchase=2007,
        price=100000,
    )
    instrument_item_2 = InstrumentItem(
        id=2,
        instrument_id=9,
        serial_number="211.311",
        description="China",
        year_of_purchase=2017,
        price=123000,
    )
    instrument_item_3 = InstrumentItem(
        id=3,
        instrument_id=8,
        serial_number="211.221.1",
        description="Greece",
        year_of_purchase=2019,
        price=345000,
    )
    instrument_item_4 = InstrumentItem(
        id=4,
        instrument_id=7,
        serial_number="211.221-7",
        description="Curdo-persiano",
        year_of_purchase=2024,
        price=875000,
    )
    instrument_item_5 = InstrumentItem(
        id=5,
        instrument_id=6,
        serial_number="211.221-8",
        description="Thailand",
        year_of_purchase=1997,
        price=986000,
    )
    instrument_item_6 = InstrumentItem(
        id=6,
        instrument_id=5,
        serial_number="111.24",
        description="India",
        year_of_purchase=1998,
        price=197000,
    )
    instrument_item_7 = InstrumentItem(
        id=7,
        instrument_id=4,
        serial_number="111.212",
        description="Okinawa",
        year_of_purchase=2000,
        price=75000,
    )
    instrument_item_8 = InstrumentItem(
        id=8,
        instrument_id=3,
        serial_number="111.242.222",
        description="Mexico",
        year_of_purchase=2002,
        price=84000,
    )
    instrument_item_9 = InstrumentItem(
        id=9,
        instrument_id=2,
        serial_number="423.121.22",
        description="Portugal",
        year_of_purchase=2004,
        price=468000,
    )
    instrument_item_10 = InstrumentItem(
        id=10,
        instrument_id=21,
        serial_number="56.211.2",
        description="Cambodia",
        year_of_purchase=2007,
        price=47600,
    )
    instrument_item_11 = InstrumentItem(
        id=11,
        instrument_id=20,
        serial_number="2451.211.2",
        description="Cambodia",
        year_of_purchase=2019,
        price=886000,
    )
    instrument_item_12 = InstrumentItem(
        id=12,
        instrument_id=19,
        serial_number="1341.311",
        description="China",
        year_of_purchase=2017,
        price=123000,
    )
    instrument_item_13 = InstrumentItem(
        id=13,
        instrument_id=18,
        serial_number="451.221.1",
        description="Greece",
        year_of_purchase=2019,
        price=345000,
    )
    instrument_item_14 = InstrumentItem(
        id=14,
        instrument_id=17,
        serial_number="56.221-7",
        description="Curdo-persiano",
        year_of_purchase=2024,
        price=87000,
    )
    instrument_item_15 = InstrumentItem(
        id=15,
        instrument_id=16,
        serial_number="242.221-8",
        description="Thailand",
        year_of_purchase=1999,
        price=500000,
    )
    instrument_item_16 = InstrumentItem(
        id=16,
        instrument_id=15,
        serial_number="545.24",
        description="India",
        year_of_purchase=1789,
        price=190000,
    )
    instrument_item_17 = InstrumentItem(
        id=17,
        instrument_id=14,
        serial_number="35.212",
        description="Okinawa",
        year_of_purchase=2000,
        price=750000,
    )
    instrument_item_18 = InstrumentItem(
        id=18,
        instrument_id=13,
        serial_number="134.242.222",
        description="Mexico",
        year_of_purchase=2002,
        price=840000,
    )
    instrument_item_19 = InstrumentItem(
        id=19,
        instrument_id=12,
        serial_number="46.121.22",
        description="Portugal",
        year_of_purchase=2003,
        price=68000,
    )
    db_session.add_all(
        [
            instrument_item_1,
            instrument_item_2,
            instrument_item_3,
            instrument_item_4,
            instrument_item_5,
            instrument_item_6,
            instrument_item_7,
            instrument_item_8,
            instrument_item_9,
            instrument_item_10,
            instrument_item_11,
            instrument_item_12,
            instrument_item_13,
            instrument_item_14,
            instrument_item_15,
            instrument_item_16,
            instrument_item_17,
            instrument_item_18,
            instrument_item_19,
        ]
    )
    db_session.commit()


def add_customer_order():
    customer_order_1 = CustomerOrder(
        id=1,
        customer_name="Trang",
        delivery_address="95 Le Van Sy",
        phone_number="0392391585",
        order_time=datetime(2012, 3, 7, 10, 20, 27, 6),
        total_price=1978000,
    )
    customer_order_2 = CustomerOrder(
        id=2,
        customer_name="Kemi",
        delivery_address="Bui Thi Xa",
        phone_number="039244585",
        order_time=datetime(2014, 8, 3, 14, 10, 29, 7),
        total_price=8047000,
    )
    customer_order_3 = CustomerOrder(
        id=3,
        customer_name="Quang",
        delivery_address="Truong Sa",
        phone_number="03945691585",
        order_time=datetime(2023, 10, 12, 19, 10, 23, 9),
        total_price=3294000,
    )
    customer_order_4 = CustomerOrder(
        id=4,
        customer_name="Max",
        delivery_address="Hoang Sa",
        phone_number="0392391585",
        order_time=datetime(2022, 12, 23, 18, 10, 32, 10),
        total_price=1099000,
    )
    customer_order_5 = CustomerOrder(
        id=5,
        customer_name="Dat",
        delivery_address="Nguyen Thuong Hien",
        phone_number="0342391585",
        order_time=datetime(2020, 10, 3, 7, 10, 14, 9),
        total_price=204000,
    )
    customer_order_6 = CustomerOrder(
        id=6,
        customer_name="Linh Ng",
        delivery_address="20 Phu Nhuan",
        phone_number="0562391585",
        order_time=datetime(2017, 5, 3, 15, 10, 8, 5),
        total_price=1725000,
    )
    customer_order_7 = CustomerOrder(
        id=7,
        customer_name="Trung",
        delivery_address="Ho Chi Minh",
        phone_number="03392391585",
        order_time=datetime(2012, 6, 3, 17, 10, 17, 4),
        total_price=1140000,
    )
    customer_order_8 = CustomerOrder(
        id=8,
        customer_name="Pham",
        delivery_address="Ea street",
        phone_number="0672391585",
        order_time=datetime(2012, 7, 4, 18, 10, 15, 6),
        total_price=2520000,
    )
    customer_order_9 = CustomerOrder(
        id=9,
        customer_name="Ngan",
        delivery_address="Quan 8",
        phone_number="03672391585",
        order_time=datetime(2019, 3, 27, 10, 20, 30, 10),
        total_price=345000,
    )
    customer_order_10 = CustomerOrder(
        id=10,
        customer_name="Ngoc",
        delivery_address="Cho ban co",
        phone_number="0232391585",
        order_time=datetime(2020, 3, 29, 7, 10, 27, 3),
        total_price=174000,
    )
    customer_order_11 = CustomerOrder(
        id=11,
        customer_name="Minh",
        delivery_address="Ba Chieu",
        phone_number="0423391585",
        order_time=datetime(2009, 3, 3, 10, 9, 30, 5),
        total_price=100000,
    )
    db_session.add_all(
        [
            customer_order_1,
            customer_order_2,
            customer_order_3,
            customer_order_4,
            customer_order_5,
            customer_order_6,
            customer_order_7,
            customer_order_8,
            customer_order_9,
            customer_order_10,
            customer_order_11,
        ]
    )
    db_session.commit()


def add_order_item():
    order_item_1 = OrderItem(
        id=1, instrument_item_id=1, quantity=5, price=500000, customer_order_id=1
    )
    order_item_2 = OrderItem(
        id=2, instrument_item_id=2, quantity=2, price=246000, customer_order_id=1
    )
    order_item_3 = OrderItem(
        id=3, instrument_item_id=3, quantity=3, price=1035000, customer_order_id=1
    )
    order_item_4 = OrderItem(
        id=4, instrument_item_id=4, quantity=7, price=6125000, customer_order_id=2
    )
    order_item_5 = OrderItem(
        id=5, instrument_item_id=5, quantity=3, price=2958000, customer_order_id=3
    )
    order_item_6 = OrderItem(
        id=6, instrument_item_id=11, quantity=2, price=1772000, customer_order_id=2
    )
    order_item_7 = OrderItem(
        id=7, instrument_item_id=12, quantity=7, price=861000, customer_order_id=4
    )
    order_item_8 = OrderItem(
        id=8, instrument_item_id=10, quantity=5, price=238000, customer_order_id=4
    )
    order_item_9 = OrderItem(
        id=9, instrument_item_id=8, quantity=4, price=336000, customer_order_id=3
    )
    order_item_10 = OrderItem(
        id=10, instrument_item_id=7, quantity=2, price=150000, customer_order_id=2
    )
    order_item_11 = OrderItem(
        id=11, instrument_item_id=6, quantity=1, price=197000, customer_order_id=1
    )

    order_item_12 = OrderItem(
        id=12, instrument_item_id=19, quantity=3, price=204000, customer_order_id=5
    )

    order_item_13 = OrderItem(
        id=13, instrument_item_id=16, quantity=6, price=1140000, customer_order_id=7
    )

    order_item_14 = OrderItem(
        id=14, instrument_item_id=13, quantity=5, price=1725000, customer_order_id=6
    )

    order_item_15 = OrderItem(
        id=15, instrument_item_id=11, quantity=1, price=886000, customer_order_id=7
    )

    order_item_16 = OrderItem(
        id=16, instrument_item_id=18, quantity=3, price=2520000, customer_order_id=8
    )
    order_item_17 = OrderItem(
        id=17, instrument_item_id=13, quantity=1, price=345000, customer_order_id=9
    )
    order_item_18 = OrderItem(
        id=18, instrument_item_id=14, quantity=2, price=174000, customer_order_id=10
    )
    order_item_19 = OrderItem(
        id=19, instrument_item_id=1, quantity=1, price=100000, customer_order_id=11
    )
    db_session.add_all(
        [
            order_item_1,
            order_item_2,
            order_item_3,
            order_item_4,
            order_item_5,
            order_item_6,
            order_item_7,
            order_item_8,
            order_item_9,
            order_item_10,
            order_item_11,
            order_item_12,
            order_item_13,
            order_item_14,
            order_item_15,
            order_item_16,
            order_item_17,
            order_item_18,
            order_item_19,
        ]
    )
    db_session.commit()


def seed_all_data():
    add_category_data()
    add_manufacturer_data()
    add_instrument()
    add_instrucment_item()
    add_customer_order()
    add_order_item()
    with open("initialized.flag", "w") as flag_file:
        flag_file.write("initialized")
