# from flask import Flask,render_template,request
# from flask_sqlalchemy import SQLAlchemy
#
# app =Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# db = SQLAlchemy(app)
#
# # class Message(db.Model):
# #     id=db.Column(db.Integer,primary_key=True)
# #     data=db.Column(db.String(200),primary_key=False)
#
# class Pizza(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.String(200),primary_key=False)
#     photo_urls = db.Column(db.String(200),primary_key=False)

# db.create_all()



import sqlite3
conn = sqlite3.connect("pizza.db")
columns = [
    "id INTEGER PRIMARY KEY",
    "name VARCHAR UNIQUE",
   "urls VARCHAR", ]
# create_table_cmd = f"CREATE TABLE pizza ({','.join(columns)})"
# conn.execute(create_table_cmd)
conn.execute("INSERT into pizza values (1,'Pepperoni','some url')")
conn.commit()
cur=conn.cursor()
cur.execute('select * from pizza')
answer=cur.fetchall()
print(answer)


# del_table_cmd = f"drop TABLE person"