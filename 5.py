import sys


characters = [
('a',188461),
('b',565383),
('d',696149),
('e',88447),
('g',265341),
('h',796023),
('i',388069),
('l',164207),
('n',492621),
('o',477863),
('s',433589),
('t',300767),
('u',902301)
]

MAX_LENGTH = 3

def print_chars(chars) :
    output = ''
    for c in chars :
        output = output + c[0]
    return output

def is_valid(chars, n) :
    total = 0
    for char in chars :
        total = total + char[1]
    return str(total).endswith(n)

def find_combination(current_chars,n) :
    if len(current_chars) >= MAX_LENGTH :
        return
    for c in characters :
        new_chars = current_chars + [c]
        if (is_valid(new_chars,n)) :
            print print_chars(new_chars)
        find_combination(new_chars,n)

if __name__ == "__main__" :
    n = sys.argv[1]
    find_combination([],n)
