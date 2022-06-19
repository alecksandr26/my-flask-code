from flask_testing import TestCase
from flask import current_app, url_for
from main import app


"""
To run all the tests of the application
"""

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)


    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)


    def test_auth_return200(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)


    def test_home_return404(self):
        response = self.client.post(url_for('home'))
        self.assert405(response)
