import unittest
from app import app

class TestAnimalAPIFunctional(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_animal_rugir(self):
        self.app.post('/animals', json={'name': 'Tigre', 'action': 'rugir'})
        response = self.app.post('/animals/1/rugir')
        self.assertEqual(response.status_code, 200)
        self.assertIn('está rugiendo', str(response.data))

if __name__ == '__main__':
    unittest.main()
