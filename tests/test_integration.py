import unittest
from app import app, db_session
from models import Animal

class TestAnimalAPIIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        db_session.query(Animal).delete()

    def test_create_and_get_animal(self):
        self.app.post('/animals', json={'name': 'Tigre', 'action': 'rugir'})
        response = self.app.get('/animals')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Tigre', str(response.data))

if __name__ == '__main__':
    unittest.main()
