import unittest
from discount_calculator import calculate_discount

class InvoiceCalculatorTests(unittest.TestCase):
    def testCalculate_discount(self):
        discounted_price = calculate_discount(100,.1,20)
        #check that the right values are returned
        self.assertEqual(discounted_price, 70)
        
        discounted_price = calculate_discount(100, 0 , 0)
        #check that the right values are returned
        self.assertEqual(discounted_price, 100)

        discounted_price = calculate_discount(100, 1 , 10)
        #check that the right values are returned
        self.assertEqual(discounted_price, -10)


if __name__ == "__main__":
    unittest.main()
