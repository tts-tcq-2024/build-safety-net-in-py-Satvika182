def get_soundex_mapping():
    return {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }

def get_soundex_code(c, mapping):
    return mapping.get(c.upper(), '0')

def pad_soundex_code(soundex):
    return soundex.ljust(4, '0')

def process_name(name, mapping):
    soundex = [name[0].upper()]
    prev_code = get_soundex_code(soundex[0], mapping)
    append_code = soundex.append
    code_length = 1

    for char in name[1:]:
        code = get_soundex_code(char, mapping)
        if code != '0' and code != prev_code:
            append_code(code)
            prev_code = code
            code_length += 1
            if code_length == 4:
                break

    return ''.join(soundex)

def generate_soundex(name):
    if not name:
        return ""
    
    mapping = get_soundex_mapping()
    soundex = process_name(name, mapping)
    return pad_soundex_code(soundex)
