import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        
    def test_numerical_inputs(self):
        self.assertEqual(generate_soundex("1234"), "0000")
        self.assertEqual(generate_soundex("A1B2C3"), "A120")
        self.assertEqual(generate_soundex("Z1Y2X3"), "Z020")

    def test_mixed_cases(self):
        self.assertEqual(generate_soundex("AbC"), "A120")
        self.assertEqual(generate_soundex("aBc"), "A120")
        self.assertEqual(generate_soundex("aBCdEf"), "A132")

    
if __name__ == '__main__':
    unittest.main()
