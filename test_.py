import unittest
from main import proibido
from main import texto

class TestProibido(unittest.TestCase):
    def test_proibido(self):
        self.assertEqual(proibido(texto), len(texto) * "*")

if __name__ == "__main__":
    unittest.main()