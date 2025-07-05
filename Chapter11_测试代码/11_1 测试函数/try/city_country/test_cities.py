import unittest
from city_functions import city_country
class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        santiago_chile =city_country('Santiago','Chile')
        self.assertEqual(santiago_chile,'Santiago Chile')
if __name__ == '__main__':
    unittest.main()