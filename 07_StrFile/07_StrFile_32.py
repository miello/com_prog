pattern = ['!@#$%^&*()_+', 'QWERTYUIOP', 'ASDFGHJKL', 'ZXCVBNM']
number_seq = '01234567890'
char_seq = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def no_lower_letters(text):
    for ch in text:
        if 'a' <= ch <= 'z':
            return False
    return True


def no_upper_letters(text):
    for ch in text:
        if 'A' <= ch <= 'Z':
            return False
    return True


def no_numbers(text):
    for ch in text:
        if '0' <= ch <= '9':
            return False
    return True


def no_symbols(text):
    for ch in text:
        if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            continue
        else:
            return False
    return True


def character_repetition(text):
    for p in range(len(text) - 3):
        prev = text[p]
        chk = True
        for ch in text[p:p + 4]:
            if prev != ch:
                chk = False
                break
        if chk:
            return True
    return False


def number_sequence(text):
    for p in range(len(text) - 3):
        l = "".join(text[p:p + 4])
        if number_seq.find(l) != -1 or number_seq.find(l[::-1]) != -1:
            return True
    return False


def letter_sequence(text):
    for p in range(len(text) - 3):
        temp = ''
        for ch in text[p:p + 4]:
            if 'a' <= ch <= 'z':
                temp += chr(ord(ch) - 32)
            else:
                temp += ch
        l = "".join(temp)
        if char_seq.find(l) != -1 or char_seq.find(l[::-1]) != -1:
            return True
    return False


def keyboard_pattern(text):
    for p in range(len(text) - 3):
        temp = ''
        for ch in text[p:p + 4]:
            if 'a' <= ch <= 'z':
                temp += chr(ord(ch) - 32)
            else:
                temp += ch
        for pat in pattern:
            if pat.find(temp) != -1 or pat.find(temp[::-1]) != -1:
                return True
    return False


text = input().strip()
OK = False

if len(text) < 8:
    print('Less than 8 characters')
    OK = True
if no_lower_letters(text):
    print('No lowercase letters')
    OK = True
if no_upper_letters(text):
    print('No uppercase letters')
    OK = True
if no_numbers(text):
    print('No numbers')
    OK = True
if no_symbols(text):
    print('No symbols')
    OK = True
if character_repetition(text):
    print('Character repetition')
    OK = True
if number_sequence(text):
    print('Number sequence')
    OK = True
if letter_sequence(text):
    print('Letter sequence')
    OK = True
if keyboard_pattern(text):
    print('Keyboard pattern')
    OK = True

if not OK:
    print('OK')
