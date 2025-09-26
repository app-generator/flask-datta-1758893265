# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Networks(db.Model):

    __tablename__ = 'Networks'

    id = db.Column(db.Integer, primary_key=True)

    #__Networks_FIELDS__
    vnpt = db.Column(db.String(255),  nullable=True)
    fpt = db.Column(db.String(255),  nullable=True)
    viettel = db.Column(db.String(255),  nullable=True)
    mobi = db.Column(db.String(255),  nullable=True)
    viettel4g = db.Column(db.String(255),  nullable=True)
    vina = db.Column(db.String(255),  nullable=True)
    vpn = db.Column(db.String(255),  nullable=True)

    #__Networks_FIELDS__END

    def __init__(self, **kwargs):
        super(Networks, self).__init__(**kwargs)


class Tool_Names(db.Model):

    __tablename__ = 'Tool_Names'

    id = db.Column(db.Integer, primary_key=True)

    #__Tool_Names_FIELDS__
    mercury = db.Column(db.String(255),  nullable=True)
    venus = db.Column(db.String(255),  nullable=True)
    earth = db.Column(db.String(255),  nullable=True)
    jupiter = db.Column(db.String(255),  nullable=True)
    uranus = db.Column(db.String(255),  nullable=True)
    saturn = db.Column(db.String(255),  nullable=True)
    pluto = db.Column(db.String(255),  nullable=True)

    #__Tool_Names_FIELDS__END

    def __init__(self, **kwargs):
        super(Tool_Names, self).__init__(**kwargs)



#__MODELS__END
