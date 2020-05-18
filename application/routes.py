from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Orders, Stock
from application.forms import OrderForm, StockForm



@app.route('/')
@app.route('/home')
def home():
	OrderData = Orders.query.all()
	return render_template('home.html', title="Home Page", orders=OrderData)

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/orders', methods=['GET', 'POST'])
def order():
	form = OrderForm()
	if form.validate_on_submit():
		orderData = Orders(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			number=form.number.data,
			address=form.address.data,
			pizza=form.pizza.data,
			quantity=form.quantity.data
		)
		db.session.add(orderData)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('order.html', title='Order', form=form)	

@app.route('/stock', methods=['GET', 'POST'])
def stock():
	form - StockForm()
	if form.validate_on_submit():
		stockData = Stock(
			pizza=form.pizza.data,
			quantity=form.quantity.data
		)
		db.session.add(stockData)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('stock.html', title='stock', form=form)
	