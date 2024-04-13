import unittest
from flask_testing import TestCase
from app import app, boggle_game

class FlaskTestCase(TestCase):

    def create_app(self):
        # Configure your application for testing
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SECRET_KEY'] = 'test_secret'
        return app

    def setUp(self):
        # Called before every test, good place to setup the board
        self.client = app.test_client()
        self.client.application.config['TESTING'] = True
        with self.client as c:
            with c.session_transaction() as sess:
                sess['board'] = [
                    ["t", "e", "s", "t", "s"],
                    ["a", "b", "c", "d", "e"],
                    ["f", "g", "h", "i", "j"],
                    ["k", "l", "m", "n", "o"],
                    ["p", "q", "r", "s", "t"]
                ]


    def test_word_found(self):
        # Test word found on the board
        
        response = self.client.get('/check-word?word=test')
        print(response.json['result'] == 'ok')
        self.assertEqual(response.json['result'], 'ok')

    def test_word_not_found(self):
        # Test word not found on the board
        response = self.client.get('/check-word?word=python')
        self.assertEqual(response.json['result'], 'not-on-board')

    def test_invalid_word(self):
        # Test word which is not valid (not in dictionary)
        response = self.client.get('/check-word?word=xyz')
        self.assertEqual(response.json['result'], 'not-a-word')

if __name__ == '__main__':
    unittest.main()