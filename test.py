import unittest
from models import Rent,Company


class TestCompany(unittest.TestCase):

    def test_company(self):
        my_company = Company()

        #Creating Simple Rents
        my_company.add_rent(15,"hours")
        my_company.add_rent(15,"days")
        my_company.add_rent(15,"weeks")

        #Creating Promotions
        my_company.add_promotion([Rent(10,"hours"),Rent(10,"hours"),Rent(10,"hours"),Rent(5,"hours")])
        my_company.add_promotion([Rent(10,"days"),Rent(10,"days"),Rent(10,"days"),Rent(5,"days")])
        my_company.add_promotion([Rent(10,"weeks"),Rent(10,"weeks"),Rent(10,"weeks"),Rent(5,"weeks")])
        my_company.add_promotion([Rent(10,"hours"),Rent(10,"days"),Rent(10,"weeks")])

        #Verify coverage
        self.assertGreaterEqual(85, my_company.coverage())


if __name__ == '__main__':
    unittest.main()