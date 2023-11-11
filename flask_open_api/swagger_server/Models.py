from swagger_server.db import db
# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from sqlalchemy import Enum
from sqlalchemy import UUID
import enum
class PizzaDB(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),primary_key=False)
    photo_urls = db.Column(db.String(200),primary_key=False)
    price=db.Column(db.Float,primary_key=False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'photo_urls': self.photo_urls,'price': self.price}


    def __repr__(self):
        return '<Message %r' % self.id
class Status(enum.Enum):
    in_progress=1
    ready=2
    delivered=3
class OrderDB(db.Model):
    # id = db.Column(db.Integer,primary_key=True)
    Price = db.Column(db.Integer, primary_key=False)
    # id=db.Column(UUID(as_uuid=True),primary_key=True,server_default=sa_text("uuid_generate_v4()"),)
    id = db.Column(db.String(200), primary_key=True )
    address=db.Column(db.String(200),primary_key=False)
    # status = db.Column(db.String(200), primary_key=False)
    status=db.Column(Enum(Status),primary_key=False)
    # def __repr__(self):
    #     return '<Message %r' % self.id

class PositionInOrderDB(db.Model):
    # id = db.Column(db.Integer,primary_key=True)
    order_uuid = db.Column(db.String(200),db.ForeignKey('order_db.id'))
    # uuid = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"), )
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    id_pizza = db.Column(db.Integer,primary_key=False)
    count = db.Column(db.Integer,primary_key=False)

    def __repr__(self):
        return '<Message %r' % self.id

