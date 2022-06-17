from flask_testing import TestCase
from flask import current_app
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
        
