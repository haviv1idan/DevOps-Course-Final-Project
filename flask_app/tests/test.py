import unittest
from unittest.mock import patch
from flask_app.src.app import app, api  # Import both the Flask app and the API instance

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a test client for the Flask app"""
        app.testing = True
        self.client = app.test_client()

    @patch.object(api, 'get_questions', return_value=[{"question": "Sample?", "answer": "Example"}])
    def test_questions_endpoint(self, mock_get_questions):
        """Test the /questions endpoint with a mocked API response"""
        response = self.client.get('/questions')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": [{"question": "Sample?", "answer": "Example"}]})

        # Ensure the mock method was called once
        mock_get_questions.assert_called_once()

if __name__ == '__main__':
    unittest.main()
