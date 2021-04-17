import unittest
from src.googleScrapy import Google

class TestGoogleSerpSearch(unittest.TestCase):

    def test_search(self):

        result = Google().search('milk')
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()