import unittest
from models import Rent,Company


class TestCompany(unittest.TestCase):

    def test_company(self):
        my_company = Company()
        #Creating Bikes
        for i in range(17):
            my_company.add_bike(i)

        #Creating Rents
        my_company.add_rent(15,"hours",1)
        my_company.add_rent(15,"days",2)
        my_company.add_rent(15,"weeks",3)

        #Creating Promotions
        my_company.add_promotion([Rent(10,"hours",4),Rent(10,"hours",5),Rent(10,"hours",6),Rent(5,"hours",7)])
        my_company.add_promotion([Rent(10,"days",11),Rent(10,"days",10),Rent(10,"days",9),Rent(5,"days",8)])
        my_company.add_promotion([Rent(10,"weeks",12),Rent(10,"weeks",13),Rent(10,"weeks",14),Rent(5,"weeks",15)])
        my_company.add_promotion([Rent(10,"hours",18),Rent(10,"days",17),Rent(10,"weeks",16)])

        #Verify coverage
        self.assertLess(85, my_company.coverage())


if __name__ == '__main__':
    unittest.main()