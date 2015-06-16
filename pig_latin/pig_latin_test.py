from pig_latin import pig_latin
import unittest


class TestPiggyLatin(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_does_the_latin_pig(self):
        self.assertEqual(pig_latin("pig"),"igpay")
        
    def test_does_the_latin_banana(self):
        self.assertEqual(pig_latin("banana"),"ananabay")
        

    def test_does_the_latin_trash(self):
        self.assertEqual(pig_latin("trash"),"rashtay")
        
    def test_does_the_latin_happy(self):
        self.assertEqual(pig_latin("happy"),"appyhay")
        
    def test_does_the_latin_duck(self):
        self.assertEqual(pig_latin("duck"),"uckday")
        
    def test_does_the_latin_glove(self):
        self.assertEqual(pig_latin("glove"),"oveglay")
        
    def test_does_the_latin_egg(self):
        self.assertEqual(pig_latin("egg"),"eggway")


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
