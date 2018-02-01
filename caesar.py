def rotate_string(text,rot):

    output = ""
    for i in range(0,len(text)):
        output = output + rotate_character(text[i],rot)

    return output

def alphabet_position(users_letter):

    alphabet = []
    for i in range(97,123):
        alphabet.append(chr(i))

    upper_alphabet = []
    for i in range(65, 91):
        upper_alphabet.append(chr(i))

    for i in range(0,len(alphabet)):
        if users_letter == alphabet[i]:
            return i

    for i in range(0,len(upper_alphabet)):
        if users_letter == upper_alphabet[i]:
            return i

def rotate_character(char, rot):

    alphabet = []
    for i in range(97,123):
        alphabet.append(chr(i))

    upper_alphabet = []
    for i in range(65, 91):
        upper_alphabet.append(chr(i))

    if char.isalpha():
        new_position = alphabet_position(char) + int(rot)

        while new_position > 25 or new_position < 0:
            if new_position > 25:
                new_position = new_position - 26
            elif new_position < 0:
                new_position = new_position + 26

    if char.isupper():
        return upper_alphabet[new_position]
    elif char.islower():
        return alphabet[new_position]
    else:
        return char


