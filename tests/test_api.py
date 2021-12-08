# import unittest
# import selenium

POSITIVE = "Positive"
NEGATIVE = "Negative"
NEUTRAL = "Neutral"

tests = {"I like apples" : POSITIVE, "I don't like apples" : NEGATIVE, "My name is Omar" : NEUTRAL}

# class Tests(unittest.TestCase):

#     def test(self):
#         for sentence, exp_sentiment in tests.items():
#             pass



# if __name__ == '__main__':
#     unittest.main()

from selenium.webdriver.common import by
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basics(self):
        url = "http://host.docker.internal:8501"
        for sentence, exp_sentiment in tests.items():
            self.open(url)
            self.type('textarea', sentence)
            print(self.get_text("textarea"))
            self.click("//*[text()[contains(., 'Analyze')]]", by=by.By.XPATH)
            print(self.get_text("div[data-stale='false'] > div > div > p"))
            self.assert_text(exp_sentiment, "div[data-stale='false'] > div > div > p")