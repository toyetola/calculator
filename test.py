import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_calculator(self):

        #Test 1: Passing the input and using other methods
        newcalculator = calculator("7+4+3")

        #sanitizing input
        evaluteSanitizedInput = newcalculator.sanitizeString()

        #evaluating input
        retunedAnswer = newcalculator.bodmasConsistency(evaluteSanitizedInput)
        self.assertEqual(retunedAnswer, 14.0, "should be 14")

    def test_calculator2(self):
        newcalculator = calculator("2+3-3")
        
        evaluteSanitizedInput = newcalculator.sanitizeString()
        
        retunedAnswer = newcalculator.bodmasConsistency(evaluteSanitizedInput)
        
        self.assertEqual(retunedAnswer, 2, "should be 2")

    def test_calculator3(self):
        newcalculator = calculator("5/2-3")
        evaluteSanitizedInput = newcalculator.sanitizeString()
        retunedAnswer = newcalculator.bodmasConsistency(evaluteSanitizedInput)
        self.assertEqual(retunedAnswer, -0.5, "should be -0.5")

    def test_calculator4(self):
        newcalculator = calculator("10+4-5*2/2")
        evaluteSanitizedInput = newcalculator.sanitizeString()
        retunedAnswer = newcalculator.bodmasConsistency(evaluteSanitizedInput)
        self.assertEqual(retunedAnswer, 9, "should be 9")
        
if __name__ == '__main__':
    unittest.main()
    
