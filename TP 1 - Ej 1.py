import string
def char_is_alnum(str):
    for i in str:
        if i.isalnum():
            return True
    return False

def find_a_letter(string):
    for i in (string):
        if i in string:
            return True
    return False

def char_length(str):
    length = len(str)
    if length >= 8:
        return True
    else:
        return False

def char_is_upper(str):
    for i in str:
        if i.isupper():
            return True
    return False

def char_is_lower(str):
    for i in str:
        if i.islower():
            return True
    return False

def char_is_digit(str):
    for i in str:
        if i.isdigit():
            return True
    return False

def validate_string(str):
    word = str
    alpha = char_is_alnum(word)
    isletter = find_a_letter(word)
    upper = char_is_upper(word)
    lower = char_is_lower(word)
    digit = char_is_digit(word)
    char_len = char_length(word)
    return alpha, isletter, upper, lower, digit, char_len

word = str(input("Ingrese una palabra: "))
function = validate_string(word)
for i in function:
    print(i)

  
