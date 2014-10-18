import unittest
from invoice_calculator import divide_pay

class InvoiceCalculatorTests(unittest.TestCase):
    def testDividedFairly(self):
        pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 3.0, "Joyce": 3.0})
        #check that the right values are returned
        self.assertEqual(pay, {"Alice":90.0, "Bob": 90.0, "Carol": 90.0, "Joyce": 90.0})
        
        pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0, "Joyce": 0.0})
        # Check that the right values are returned
        self.assertEqual(pay, {"Alice": 90.0, "Bob": 90.0, "Carol": 180.0, "Joyce": 0.0})

        pay = divide_pay(360.0, {"Alice": 0.0, "Bob": 0.0, "Carol": 0.0, "Joyce": 0.0})
        # Check that the right values are returned
        self.assertEqual(pay, {"Alice": 0, "Bob": 0, "Carol": 0, "Joyce": 0.0})

    def testNoPeople(self):
        with self.assertRaises(ValueError):
            pay = divide_pay(360.0, {})

if __name__ == "__main__":
    unittest.main()
