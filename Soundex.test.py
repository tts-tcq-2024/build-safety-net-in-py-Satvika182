import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    #def test_empty_string(self):
    #    self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("Z"), "Z000")

    def test_special_characters(self):
        self.assertEqual(generate_soundex("A#B"), "A200")
        self.assertEqual(generate_soundex("B@!#"), "B100")
        
    def test_words(self):
        self.assertEqual(generate_soundex("Satvika"), "S312")

    
if __name__ == '__main__':
    unittest.main()
