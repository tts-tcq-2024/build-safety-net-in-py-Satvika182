import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    # def test_empty_string(self):
    #     self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")

    def test_special_characters(self):
        self.assertEqual(generate_soundex("A#B"), "A100")
        self.assertEqual(generate_soundex("B@!#"), "B000")
        
    def test_words(self):
        self.assertEqual(generate_soundex("Smith"), "S530")

    
if __name__ == '__main__':
    unittest.main()
