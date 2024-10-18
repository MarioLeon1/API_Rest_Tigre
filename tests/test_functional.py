import unittest
from app import app

class TestAnimalAPIFunctional(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_animal_rugir(self):
        # Crear un animal en la base de datos de pruebas
        self.app.post('/animals', json={'name': 'Tigre', 'action': 'rugir'})
        
        # Realizar la solicitud POST al endpoint de rugir
        response = self.app.post('/animals/1/rugir')
        
        # Decodificar la respuesta de bytes a una cadena usando UTF-8
        self.assertIn('está rugiendo', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
