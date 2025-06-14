import datetime

leet_map = {
    'a': ['a', '@', '4'],
    'e': ['e', '3'],
    'i': ['i', '1', '!'],
    'o': ['o', '0'],
    's': ['s', '$', '5'],
    't': ['t', '7'],
}

def leetspeak_variants(word):
    variants = ['']
    for char in word.lower():
        substitutions = leet_map.get(char, [char])
        variants = [prev + sub for prev in variants for sub in substitutions]
    return set(variants)

def capitalization_variants(word):
    return {word, word.lower(), word.upper(), word.capitalize()}

def year_suffixes():
    current = datetime.datetime.now().year
    return ['', '123', '!', '@', '#', str(current), str(current - 1), str(current - 2)]
