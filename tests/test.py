import unittest
from app import app

class TestMockInterview(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Your Mock Interview', response.data)

    def test_start_interview_route(self):
        # Test the start_interview route
        data = {
            'fullName': 'John Doe',
            'company': 'Google',
            'Language': 'Python',
            'apiKey': ''  # Replace with a valid API key for testing
        }
        response = self.app.post('/start_interview', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'question', response.data)
        self.assertIn(b'time_limit', response.data)

    def test_check_code_route(self):
        # Test the check_code route
        data = {
            'code': 'print("hello)',
            'questionNumber': '0'
        }
        response = self.app.post('/check_code', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'correct', response.data)

if __name__ == '__main__':
    unittest.main()
