from application import db
from datetime import datetime

class Orders(db.Model):
	orderid = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	number = db.Column(db.String(30), nullable=False)
	address = db.Column(db.String(100), nullable=False)
	pizzaid = db.Column(db.Integer, db.ForeignKey('stock.pizzaid')) # should this be stock
	order_quantity = db.Column(db.Integer, nullable=False) ####### integer
	price = db.Column(db.Integer, nullable=False) ######## times by price per pizza

class Stock(db.Model):
	pizzaid = db.Column(db.Integer, primary_key=True)
	stock_quantity = db.Column(db.Integer, nullable=False) ###########)
	priceperpizza = db.Column(db.Integer, nullable=False)
	orders = db.relationship('Orders', backref='pizza', lazy=True)

