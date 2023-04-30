import unittest

from translator import english_to_french, french_to_english

class TestEnglishtofrench(unittest.TestCase):
    '''Tests English to French function'''
    def test1(self):
        '''Tests null, hello and Thank You translations'''
        self.assertEqual(english_to_french(None), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Yes'), 'Oui')

class TestEnglishtogerman(unittest.TestCase):
    '''Tests French to English function'''
    def test1(self):
        '''Tests null, hello and Thank You translations'''
        self.assertEqual(french_to_english(None), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Oui'), 'Yes')

unittest.main()