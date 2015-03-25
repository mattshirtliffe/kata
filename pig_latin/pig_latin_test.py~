from fizzbuzz import fizz_buzzy
import unittest


class TestFizzyBuzzy(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_does_fizz(self):
        self.assertEqual(fizz_buzzy(3),"Fizz")

    def test_does_buzz(self):
        self.assertEqual(fizz_buzzy(5),"Buzz")

    def test_does_fizzbuzz(self):
        self.assertEqual(fizz_buzzy(90),"FizzBuzz")

    def test_does_other(self):
        self.assertEqual(fizz_buzzy(1),"1")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
