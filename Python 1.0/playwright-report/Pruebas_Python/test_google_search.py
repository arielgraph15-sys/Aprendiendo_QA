import unittest
from main import google_search

class TestGoogleSearch(unittest.TestCase):
    # Test para verificar que la busqueda de goole son correctas
    def test_valid_query(self):
        """Prueba con una consulta valida"""
        self.assertEqual(google_search("python"),["python.org", "tutorial python", "aprender python"],)

    def test_invalid_query(self):
        """Prueba con una consulta invalida"""
        self.assertEqual(google_search("hola"), ['hola'])
        

        if __name__ == "__main__":
            unittest.main()

