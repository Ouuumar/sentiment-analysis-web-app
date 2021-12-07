import unittest
import requests

POSITIVE = "Positive"
NEGATIVE = "Negative"
NEUTRAL = "Neutral"

tests = {"I like apples" : POSITIVE, "I don't like apples" : NEGATIVE, "My name is Omar" : NEUTRAL}

class Tests(unittest.TestCase):

    def test(self):
        for sentence, exp_sentiment in tests.items():
            pass



if __name__ == '__main__':
    unittest.main()
