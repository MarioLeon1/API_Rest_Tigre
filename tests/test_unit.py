import unittest
from app import app

class TestAnimalAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_animals(self):
        response = self.app.get('/animals')
        self.assertEqual(response.status_code, 200)

    def test_create_animal(self):
        response = self.app.post('/animals', json={'name': 'Tigre', 'action': 'rugir'})
        self.assertEqual(response.status_code, 201)

    def test_animal_not_found(self):
        response = self.app.get('/animals/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
