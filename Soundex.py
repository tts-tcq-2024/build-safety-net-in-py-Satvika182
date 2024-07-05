def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters

def initialize_soundex(name):
    if not name:
        return "", ""
    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def should_update_soundex(code, prev_code):
    return code != '0' and code != prev_code

def update_soundex(char, prev_code, soundex):
    code = get_soundex_code(char)
    if should_update_soundex(code, prev_code):
        soundex += code
        prev_code = code
    return prev_code, soundex

def char_generator(name):
    for char in name[1:]:
        yield char

def process_name_chars(name, soundex, prev_code):
    for char in char_generator(name):
        if len(soundex) >= 4:
            break
        prev_code, soundex = update_soundex(char, prev_code, soundex)
    return soundex, prev_code

def pad_soundex(soundex):
    return soundex.ljust(4, '0')

def generate_soundex(name):
    if not name:
        return "0000"

    soundex, prev_code = initialize_soundex(name)
    soundex, _ = process_name_chars(name, soundex, prev_code)
    return pad_soundex(soundex)
