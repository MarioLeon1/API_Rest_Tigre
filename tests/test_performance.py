import unittest
import time
from app import app

class TestAnimalAPIPerformance(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_response_time(self):
        start_time = time.time()
        self.app.get('/animals')
        response_time = time.time() - start_time
        self.assertTrue(response_time < 0.5)  # La API debe responder en menos de 500ms

if __name__ == '__main__':
    unittest.main()
