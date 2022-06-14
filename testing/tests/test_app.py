from flask_testing import TestCase
from flask import current_app, url_for
from app import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SECRET_KEY'] = 'mykey'
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)


    def test_home_redirect(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(url_for('hello'), response.location)
        

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assert200(response)


