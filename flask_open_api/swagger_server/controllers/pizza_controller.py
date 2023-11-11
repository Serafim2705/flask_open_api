import connexion
import six
from flask_sqlalchemy import SQLAlchemy
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.pizza import Pizza  # noqa: E501
from swagger_server.models.pizzas import Pizzas  # noqa: E501
from swagger_server import util
from swagger_server.Models import *
from swagger_server.db import db
import json
def add_pizza(body):  # noqa: E501


    if connexion.request.is_json:
        body = Pizza.from_dict(connexion.request.get_json())  # noqa: E501


    print(body)
    try:
        pizzadb=PizzaDB(id=body.id,name=body.name,photo_urls=body.photo_urls[0],price=body.price)

        db.session.add(pizzadb)
        db.session.commit()
    except:
        return "not correct input",400

    # Pizza[body.id]=body
    print(Pizza.name)
    return pizzadb.name +" success added!" ,200





def delete_pizza(pizza_id, api_key=None):  # noqa: E501


    pizza=PizzaDB.query.filter(PizzaDB.id==pizza_id).first()
    if(pizza==None):
        return 'This pizza does not exist',404
    db.session.delete(pizza)
    db.session.commit()
    return pizza.name +' has been deleted!'


def get_pizza_by_id(pizza_id):  # noqa: E501


    pizza=PizzaDB.query.filter(PizzaDB.id==pizza_id).first()
    resp={'id':pizza.id,'name':pizza.name,'photo_urls':pizza.photo_urls}
    print(resp)


    return resp,200


def pizza_get():  # noqa: E501


    print(db.metadata.tables)

    all_pizzass=PizzaDB.query.all()
    print(all_pizzass)
    pizzas=[]
    for e in all_pizzass:
        pizzas.append(dict(id=e.id,name=e.name,photoUrls=e.photo_urls,price=e.price))


    print(pizzas)
    resp={"AllPizzas":pizzas}
    print(resp)

    return resp


def update_pizza(body):  # noqa: E501


    if connexion.request.is_json:
        body = Pizza.from_dict(connexion.request.get_json())  # noqa: E501
    pizza=PizzaDB.query.filter(body.id==PizzaDB.id).first()
    print(pizza)
    if (pizza==None):
        return 'This pizza does not exist',404
    pizza.id=body.id
    pizza.name=body.name
    pizza.photo_urls=body.photo_urls[0]
    db.session.add(pizza)
    db.session.commit()

    return 'Success update!',200





def update_pizza_with_form(pizza_id, name=None, status=None):  # noqa: E501
    """Updates a pizza in the store with form data

     # noqa: E501

    :param pizza_id: ID of pizza that needs to be updated
    :type pizza_id: int
    :param name: Name of pizza that needs to be updated
    :type name: str
    :param status: Status of pizza that needs to be updated
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def upload_file(pizza_id, body=None, additional_metadata=None):  # noqa: E501
    """uploads an image

     # noqa: E501

    :param pizza_id: ID of pizza to update
    :type pizza_id: int
    :param body: 
    :type body: dict | bytes
    :param additional_metadata: Additional Metadata
    :type additional_metadata: str

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Pizza.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
