import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Orders, Stock
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLE=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        
    def test_menu_view(self):
        response = self.client.get(url_for('menu'))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_order_view(self):
        response = self.client.get(url_for('order'))
        self.assertEqual(response.status_code, 200)

    def test_orderstatus_view(self):
        response = self.client.get(url_for('orderstatus'))
        self.assertEqual(response.status_code, 200)
    
    def test_stock_view(self):
        response = self.client.get(url_for('stock'))
        self.assertEqual(response.status_code, 200)


class TestPosts(TestBase):

    def test_add_new_post(self):
        """
        Test that when I add a new post, I am redirected to the homepage with the new post visible
        """
        with self.client:
            response = self.client.post(
                '/order',
                data=dict(
                    first_name="Testy",
                    last_name="Testerson",
                    number="123456789",
                    address="64 Zoo Lane",
                    pizzaid="1",
                    order_quantity="2"
                ),
                follow_redirects=True
            )
            self.assertIn(b'Testy', response.data)