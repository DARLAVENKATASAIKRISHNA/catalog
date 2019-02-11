import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Materials(Base):
    __tablename__ = 'materials'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    menu_items = relationship("MenuItem", cascade="all,delete-orphan")

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }


class MenuItem(Base):

    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    descrption = Column(String(10))
    price = Column(String(8))
    materials_id = Column(Integer, ForeignKey('materials.id'))
    materials = relationship("Materials",
                             backref=backref("items", cascade="all,\
                             delete-orphan")
                             )
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'name': self.name,
            'descrption': self.descrption,
            'price': self.price,
            'id': self.id
        }


engine = create_engine('sqlite:///materials.db')

Base.metadata.create_all(engine)
