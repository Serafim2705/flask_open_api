#!/usr/bin/env python3

import connexion
from flask_sqlalchemy import SQLAlchemy
from swagger_server import encoder
from swagger_server.db import db
from swagger_server.Models import *
from prometheus_flask_exporter import PrometheusMetrics
from flask import request
from threading import Thread
def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Super Pizza'}, pythonic_params=True)

    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
    app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db = SQLAlchemy(app)
    metrics = PrometheusMetrics(app.app)
    db.init_app(app.app)


    app.run(port=8080)
    db.create_all()


if __name__ == '__main__':
    main()
