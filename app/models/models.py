from typing import List, Optional

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
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
    registry,
)

engine = create_engine("sqlite:///instruments.sqlite.db", echo=True)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy model classes."""

    pass


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(255), nullable=False)
    instruments: Mapped[List["Instrument"]] = relationship(
        "Instrument", back_populates="category"
    )


class Manufacturer(Base):
    __tablename__ = "manufacturer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_name = Column(String(255), nullable=False)
    instruments: Mapped[List["Instrument"]] = relationship(
        "Instrument", back_populates="manufacturer"
    )


class Instrument(Base):
    __tablename__ = "instrument"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_name = Column(String(255), nullable=False)
    manufacturer_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("manufacturer.id")
    )
    manufacturer: Mapped[Optional[Manufacturer]] = relationship(
        "Manufacturer", back_populates="instruments"
    )
    category_id: Mapped[Optional[int]] = mapped_column(ForeignKey("category.id"))
    category: Mapped[Optional[Category]] = relationship(
        "Category", back_populates="instruments"
    )
    description = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    instrument_item: Mapped[List["InstrumentItem"]] = relationship(
        "InstrumentItem", back_populates="instrument"
    )


class InstrumentItem(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    instrument_id: Mapped[int] = mapped_column(ForeignKey("instrument.id"))
    instrument: Mapped[Instrument] = relationship(
        "Instrument", back_populates="instrument_item"
    )
    serial_number = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    year_of_purchase = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)


class OrderStatus(Base):
    __tablename__ = "order_status"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    order: Mapped[List["CustomerOrder"]] = relationship(
        "CustomerOrder", back_populates="order_status"
    )
    customer_order: Mapped[List["CustomerOrder"]] = relationship(
        "CustomerOrder", back_populates="order_status"
    )


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True, unique=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    customer_order: Mapped[List["CustomerOrder"]] = relationship(
        "CustomerOrder", back_populates="customer"
    )


class OrderItem(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))
    item: Mapped[InstrumentItem] = relationship("InstrumentItem")
    quantity = Column(Integer, nullable=False)
    price = Column(Double, nullable=False)
    customer_order_id: Mapped[int] = mapped_column(ForeignKey("customer_order.id"))
    customer_order: Mapped["CustomerOrder"] = relationship(
        "CustomerOrder", back_populates="order_item"
    )


class CustomerOrder(Base):
    __tablename__ = "customer_order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    customer: Mapped[Customer] = relationship(
        "Customer", back_populates="customer_order"
    )
    order_time = Column(DateTime, nullable=False)
    preferred_delivery_time = Column(DateTime, nullable=False)
    order_status_id: Mapped[int] = mapped_column(ForeignKey("order_status.id"))
    order_status: Mapped[OrderStatus] = relationship(
        "OrderStatus", back_populates="customer_order"
    )
    time_paid = Column(DateTime, nullable=True)
    time_cancelled = Column(DateTime, nullable=True)
    time_delivered = Column(DateTime, nullable=True)
    time_completed = Column(DateTime, nullable=True)
    time_send = Column(DateTime, nullable=True)
    time_delivered_to_customer = Column(DateTime, nullable=True)
    total_price = Column(Double, nullable=False)
    delivery_address = Column(String(255), nullable=False)
    discount = Column(Double, nullable=False)
    final_price = Column(Double, nullable=False)
    active = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
metadata = Base.metadata
db_session = sessionmaker(bind=engine)()
mapper_registry = registry(metadata=metadata)

mapper_registry.configure()
# Path: entities/db_context.py
