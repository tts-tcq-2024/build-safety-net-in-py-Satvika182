import unittest
from Soundex import get_soundex_code, initialize_soundex, update_soundex, pad_soundex, process_name_chars, generate_soundex

class TestSoundexFunctions(unittest.TestCase):

    def test_initialize_soundex_empty_name(self):
        self.assertEqual(initialize_soundex(""), ("", "0"))

    def test_process_name_chars_less_than_four(self):
        self.assertEqual(process_name_chars("Smith", "S", "2"), "S2")

    def test_generate_soundex_empty_name(self):
        self.assertEqual(generate_soundex(""), "0000")

    def test_generate_soundex_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("Z"), "Z000")

    def test_generate_soundex_multiple_characters(self):
        self.assertEqual(generate_soundex("Johnson"), "J525")
        self.assertEqual(generate_soundex("Washington"), "W252")
        self.assertEqual(generate_soundex("Taylor"), "T460")

if __name__ == '__main__':
    unittest.main()
