from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import json
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String(100))


class Offer(db.Model):
    __tablename__ = "offers"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    orders = relationship("Order")
    offers = relationship("User")


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    customer = relationship("User", foreign_keys=[customer_id])
    executor = relationship("User", foreign_keys=[executor_id])


db.drop_all()
db.create_all()


with open('initial_data/users.json', encoding='utf-8') as file:
    text = file.read()
    for i in json.loads(text):
        user_x = User(
            id=i['id'],
            first_name=i['first_name'],
            last_name=i['last_name'],
            age=i['age'],
            email=i['email'],
            role=i['role'],
            phone=i['phone']
        )
        with db.session.begin():
            db.session.add(user_x)


with open('initial_data/offers.json', encoding='utf-8') as file:
    text = file.read()
    for i in json.loads(text):
        offer_x = Offer(
            id=i['id'],
            order_id=i['order_id'],
            executor_id=i['executor_id']
        )
        with db.session.begin():
            db.session.add(offer_x)


with open('initial_data/orders.json', encoding='utf-8') as file:
    text = file.read()
    for i in json.loads(text):
        start_date_list = i['start_date'].split('/')
        last_date_list = i['end_date'].split('/')
        order_x = Order(
            id=i['id'],
            name=i['name'],
            description=i['description'],
            start_date=date(
                int(start_date_list[2]),
                int(start_date_list[0]),
                int(start_date_list[1])
            ),
            end_date=date(
                int(last_date_list[2]),
                int(last_date_list[0]),
                int(last_date_list[1])
            ),
            address=i['address'],
            price=i['price'],
            customer_id=i['customer_id'],
            executor_id=i['executor_id']
        )
        with db.session.begin():
            db.session.add(order_x)


if __name__ == '__main__':
    app.run(debug=True)