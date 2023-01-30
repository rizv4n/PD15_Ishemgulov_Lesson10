from flask import Flask, render_template, request, redirect
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


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/users', methods=["GET", "POST"])
def change_users():
    if request.method == "GET":
        user_list = User.query.all()
        user_response = []

        for i in user_list:
            user_response.append(
                {
                    "id": i.id,
                    "first_name": i.first_name,
                    "last_name": i.last_name,
                    "age": i.age,
                    "email": i.email,
                    "role": i.role,
                    "phone": i.phone
                }
            )
        return json.dumps(user_response, ensure_ascii=False)
    elif request.method == "POST":
        user = User(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            age=request.form['age'],
            email=request.form['email'],
            role=request.form['role'],
            phone=request.form['phone']
        )
        with db.session.begin():
            db.session.add(user)
        count = User.query.count()
        return redirect(f'/users/{count}')


@app.route('/users/add')
def user_add_page():
    return render_template('user_post.html')


@app.route('/users/<int:sid>', methods=["GET", "PUT", "DELETE"])
def get_users(sid: int):
    if request.method == "GET":
        user = User.query.get(sid)
        if user is None:
            return "User not found"
        content = json.dumps({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "email": user.email,
            "role": user.role,
            "phone": user.phone
        }, ensure_ascii=False)
        return render_template(
            'user_page.html',
            content=content,
            user_name=f'{user.first_name} {user.last_name}',
            sid=user.id
        )
    elif request.method == "PUT":
        user = User.query.get(sid)
        content = json.dumps({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "email": user.email,
            "role": user.role,
            "phone": user.phone
        }, ensure_ascii=False)
        return render_template(
            'user_page.html',
            content=content,
            user_name=f'{user.first_name} {user.last_name}',
            sid=user.id
        )
    elif request.method == "DELETE":
        user = User.query.get(sid)
        if user is None:
            return "User not found"
        db.session.delete(user)
        db.session.commit()
        return redirect('/users')


@app.route('/offers', methods=["GET", "POST"])
def change_offers():
    if request.method == "GET":
        offer_list = Offer.query.all()
        offer_response = []

        for i in offer_list:
            offer_response.append(
                {
                    "id": i.id,
                    "order_id": i.order_id,
                    "executor_id": i.executor_id
                }
            )
        return json.dumps(offer_response)
    elif request.method == "POST":
        offer = Offer(
            order_id=request.form['order_id'],
            executor_id=request.form['executor_id']
        )
        with db.session.begin():
            db.session.add(offer)
        count = Offer.query.count() - 1
        return redirect(f'/offers/{count}')


@app.route('/offers/add')
def offer_add_page():
    return render_template('offer_post.html')


@app.route('/offers/<int:sid>', methods=["GET", "PUT", "DELETE"])
def get_offer(sid: int):
    if request.method == "GET":
        offer = Offer.query.get(sid)
        if offer is None:
            return "Offer not found"
        content = json.dumps({
            "id": offer.id,
            "order_id": offer.order_id,
            "executor_id": offer.executor_id
        })
        return render_template(
            'offer_page.html',
            content=content,
            sid=sid
        )
    elif request.method == "PUT":
        offer = Offer.query.get(sid)
        content = json.dumps({
            "id": offer.id,
            "order_id": offer.order_id,
            "executor_id": offer.executor_id
        })
        return render_template(
            'offer_page.html',
            content=content,
            sid=sid
        )
    elif request.method == "DELETE":
        offer = Offer.query.get(sid)
        if offer is None:
            return "User not found"
        db.session.delete(offer)
        db.session.commit()
        return redirect('/offers')


@app.route('/orders', methods=["GET", "POST"])
def change_orders():
    if request.method == "GET":
        order_list = Order.query.all()
        order_response = []

        for i in order_list:
            order_response.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "description": i.description,
                    "start_date": i.start_date,
                    "end_date": i.end_date,
                    "address": i.address,
                    "price": i.price,
                    "customer_id": i.customer_id,
                    "executor_id": i.executor_id
                }
            )
        return json.dumps(order_response, default=str, ensure_ascii=False)
    elif request.method == "POST":
        start_date_list = request.form['start_date'].split('-')
        last_date_list = request.form['end_date'].split('-')
        order = Order(
            name=request.form['name'],
            description=request.form['description'],
            start_date=date(
                int(start_date_list[0]),
                int(start_date_list[1]),
                int(start_date_list[2])
            ),
            end_date=date(
                int(last_date_list[0]),
                int(last_date_list[1]),
                int(last_date_list[2])
            ),
            address=request.form['address'],
            price=request.form['price'],
            customer_id=request.form['customer_id'],
            executor_id=request.form['executor_id']
        )
        with db.session.begin():
            db.session.add(order)
        count = Order.query.count() - 1
        return redirect(f'/orders/{count}')


@app.route('/orders/add')
def order_add_page():
    return render_template('order_post.html')


@app.route('/orders/<int:sid>', methods=["GET", "PUT", "DELETE"])
def get_order(sid: int):
    if request.method == "GET":
        order = Order.query.get(sid)
        if order is None:
            return "Order not found"
        content = json.dumps({
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "address": order.address,
            "price": order.price,
            "customer_id": order.customer_id,
            "executor_id": order.executor_id
        }, default=str, ensure_ascii=False)
        return render_template(
            'order_page.html',
            content=content,
            sid=sid
        )
    elif request.method == "PUT":
        order = Order.query.get(sid)
        content = json.dumps({
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "address": order.address,
            "price": order.price,
            "customer_id": order.customer_id,
            "executor_id": order.executor_id
        }, default=str, ensure_ascii=False)
        return render_template(
            'order_page.html',
            content=content,
            sid=sid
        )
    elif request.method == "DELETE":
        order = Order.query.get(sid)
        if order is None:
            return "User not found"
        db.session.delete(order)
        db.session.commit()
        return redirect('/orders')


if __name__ == '__main__':
    app.run(debug=True)
