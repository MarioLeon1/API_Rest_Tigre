import unittest
from app import app

class TestAnimalAPISecurity(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_animal_not_found(self):
        response = self.app.post('/animals/999/rugir')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
