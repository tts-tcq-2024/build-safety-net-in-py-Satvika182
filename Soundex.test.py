import unittest
from Soundex import get_soundex_code, initialize_soundex, update_soundex, pad_soundex, process_name_chars, generate_soundex

class TestSoundexFunctions(unittest.TestCase):

    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('Z'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('A'), '0')  # Non-mapped character should default to '0'

    def test_initialize_soundex_empty_name(self):
        self.assertEqual(initialize_soundex(""), ("", "0"))

    def test_initialize_soundex_non_empty_name(self):
        self.assertEqual(initialize_soundex("Johnson"), ("J", "5"))
        self.assertEqual(initialize_soundex("Washington"), ("W", "2"))

    def test_update_soundex_no_change(self):
        self.assertEqual(update_soundex("J", "2", "J"), ("2", "J"))

    def test_update_soundex_change(self):
        self.assertEqual(update_soundex("J", "2", "C"), ("2", "JC"))

    def test_pad_soundex_short_code(self):
        self.assertEqual(pad_soundex("J"), "J000")

    def test_pad_soundex_full_code(self):
        self.assertEqual(pad_soundex("JOHN"), "JOHN")

    def test_process_name_chars_less_than_four(self):
        self.assertEqual(process_name_chars("Smith", "S", "2"), "S2")

    def test_process_name_chars_more_than_four(self):
        self.assertEqual(process_name_chars("Johnson", "J", "5"), "J525")

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

