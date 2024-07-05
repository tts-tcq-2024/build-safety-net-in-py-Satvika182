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
        return "", ''
    first_letter = name[0].upper()
    return first_letter, get_soundex_code(first_letter)

def update_soundex(soundex, prev_code, char):
    code = get_soundex_code(char)
    soundex += code * (code != '0' and code != prev_code)
    prev_code = code * (code != '0' and code != prev_code) or prev_code
    return prev_code, soundex

def pad_soundex(soundex):
    return (soundex + '0000')[:4]

def process_name_chars(name, soundex, prev_code):
    updated_soundex = [soundex]
    for char in name[1:]:
        if len(updated_soundex) >= 4:
            break
        prev_code, soundex = update_soundex(soundex, prev_code, char)
        updated_soundex.append(soundex)
    return ''.join(updated_soundex)

def generate_soundex(name):
    soundex, prev_code = initialize_soundex(name)
    return pad_soundex(process_name_chars(name, soundex, prev_code))
