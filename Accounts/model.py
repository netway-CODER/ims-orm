from typing import List, Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from Accounts import Engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    password: Mapped[str]
    email: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_stuff: Mapped[bool] = mapped_column(default=False)

    addresses: Mapped[List['Address']] = relationship(back_populates='user', cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[Optional[str]]
    first_name: Mapped[Optional[str]]
    street: Mapped[str]
    city: Mapped[str] = mapped_column(default="Brossard")
    probince: Mapped[str] = mapped_column(default="Quebec")
    country: Mapped[str] = mapped_column(default="Canada")
    postal_code: Mapped[str]
    phone: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, last_name={self.last_name!r}, first_name={self.first_name!r}, street={self.street!r}, city={self.city!r}, country={self.country!r})"


Base.metadata.create_all(Engine)