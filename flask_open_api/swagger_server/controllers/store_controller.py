import connexion
import six
from flask_sqlalchemy import SQLAlchemy
from swagger_server.models.api_response import ApiResponse
from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.position_in_order import PositionInOrder  # noqa: E501
from swagger_server import util
from swagger_server.Models import *
from swagger_server.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
def delete_order(order_id):  # noqa: E501


    order=OrderDB.query.filter(OrderDB.id==order_id).first()
    positions = PositionInOrderDB.query.filter(PositionInOrderDB.id == order_id).all()
    for e in positions:
        print(e.id)
        db.session.delete(e)
    if(order==None):
        return 'This order does not exist',404
    db.session.delete(order)
    db.session.commit()
    return 'success!'


def get_order_by_id(order_id):  # noqa: E501


    all_orders=OrderDB.query.all()

    orders=[]
    for e in all_orders:
        orders.append(dict(id=e.id,Price=e.Price,address=e.address,status=str(e.status)))
        print(e.address)
    resp = {"Orders": orders}
    print(resp)
    return resp


def place_order(body=None):  # noqa: E501


    body=connexion.request.get_json()
    print(body)
    sumOfOrder=0
    newUUID = uuid.uuid4()
    print(newUUID)
    for e in body['Positions']:
        print(e['PizzaId'],e['quantity'])
        pizza = PizzaDB.query.filter(PizzaDB.id == e['PizzaId']).first()
        sumOfOrder+=pizza.price*e['quantity']
        newPos = PositionInOrderDB(order_uuid=str(newUUID),id_pizza=pizza.id,count=e['quantity'])
        db.session.add(newPos)
    print(sumOfOrder)
    newOrder=OrderDB(address=body['address'],Price=sumOfOrder,status='in_progress',id=str(newUUID))


    db.session.add(newOrder)
    db.session.commit()

    return 'do some magic!'


# def place_order(id=None, positions=None, ship_date=None, price=None, status=None, complete=None):  # noqa: E501
#     """Place an order for a pizza
#
#     Place a new order in the store # noqa: E501
#
#     :param id:
#     :type id: int
#     :param positions:
#     :type positions: list | bytes
#     :param ship_date:
#     :type ship_date: str
#     :param price:
#     :type price: float
#     :param status:
#     :type status: str
#     :param complete:
#     :type complete: bool
#
#     :rtype: Order
#     """
#     print('test!!!')
#     if connexion.request.is_json:
#         positions = [PositionInOrder.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
#         print(price)
#     ship_date = util.deserialize_datetime(ship_date)
#     return 'do some magic!'


def store_create_position_post(body=None):  # noqa: E501


    if connexion.request.is_json:
        body = PositionInOrder.from_dict(connexion.request.get_json())  # noqa: E501
        print(body)
        pizza_id=body.pizza_id
        count=body.quantity
        body.price=PizzaDB.query.filter(PizzaDB.id==pizza_id).first().price*body.quantity

        # PositionInOrderDB()
        # uuid.uuid4()
    return body


# def store_create_position_post(pizza_id=None, quantity=None, price=None, discount=None):  # noqa: E501
#     """Create positions for order
#
#     Place a new position in the order # noqa: E501
#
#     :param pizza_id:
#     :type pizza_id: dict | bytes
#     :param quantity:
#     :type quantity: int
#     :param price:
#     :type price: float
#     :param discount:
#     :type discount: float
#
#     :rtype: PositionInOrder
#     """
#     if connexion.request.is_json:
#         pizza_id = object.from_dict(connexion.request.get_json())  # noqa: E501
#     return 'do some magic!'
