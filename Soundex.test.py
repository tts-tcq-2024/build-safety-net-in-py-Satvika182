import unittest

# Assuming the Soundex code functions are defined in a file named soundex.py
from soundex import get_soundex_code, initialize_soundex, should_update_soundex, update_soundex, char_generator, process_name_chars, pad_soundex, generate_soundex

class TestSoundex(unittest.TestCase):

    def test_get_soundex_code(self):
        self.assertEqual(get_soundex_code('A'), '0')
        self.assertEqual(get_soundex_code('B'), '1')
        self.assertEqual(get_soundex_code('C'), '2')
        self.assertEqual(get_soundex_code('D'), '3')
        self.assertEqual(get_soundex_code('L'), '4')
        self.assertEqual(get_soundex_code('M'), '5')
        self.assertEqual(get_soundex_code('R'), '6')
        self.assertEqual(get_soundex_code('#'), '0')

    def test_initialize_soundex_empty(self):
        self.assertEqual(initialize_soundex(""), ("", ""))

    def test_initialize_soundex_non_empty(self):
        self.assertEqual(initialize_soundex("Johnson"), ("J", '2'))

    def test_should_update_soundex(self):
        self.assertTrue(should_update_soundex('1', '2'))
        self.assertFalse(should_update_soundex('0', '2'))
        self.assertFalse(should_update_soundex('2', '2'))

    def test_update_soundex(self):
        self.assertEqual(update_soundex('C', '2', 'J'), ('2', 'J'))
        self.assertEqual(update_soundex('S', '2', 'J2'), ('2', 'J2'))
        self.assertEqual(update_soundex('N', '2', 'J2'), ('5', 'J25'))

    def test_char_generator(self):
        gen = char_generator("Johnson")
        self.assertEqual(next(gen), 'o')
        self.assertEqual(next(gen), 'h')
        self.assertEqual(next(gen), 'n')
        self.assertEqual(next(gen), 's')
        self.assertEqual(next(gen), 'o')
        self.assertEqual(next(gen), 'n')

    def test_process_name_chars(self):
        self.assertEqual(process_name_chars("Smith", "S", "2"), ("S253", "5"))
        self.assertEqual(process_name_chars("Johnson", "J", "2"), ("J525", "5"))

    def test_pad_soundex(self):
        self.assertEqual(pad_soundex("S25"), "S250")
        self.assertEqual(pad_soundex("J52"), "J520")
        self.assertEqual(pad_soundex("R"), "R000")

    def test_generate_soundex(self):
        self.assertEqual(generate_soundex(""), "0000")
        self.assertEqual(generate_soundex("A"), "A000")
        self.assertEqual(generate_soundex("B"), "B000")
        self.assertEqual(generate_soundex("Pfister"), "P236")
        self.assertEqual(generate_soundex("Ashcraft"), "A261")
        self.assertEqual(generate_soundex("Lloyd"), "L300")

if __name__ == '__main__':
    unittest.main()
