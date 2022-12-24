#################### Morse Code Project ######################
# Objective 1: Covert Alphabets to symbolic Morse
    #A. Create dictionary with morse code patterns
    #B. Iterate over text
    #C. Print result
    #D. Solution if want to reverse from morse to text.


#A. Character Mapping
## Character to symbolic morse
CHARS_TO_SYM_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '/':'-..-.', 
    '-':'-....-',
    '(':'-.--.', 
    ')':'-.--.-',
}


# B. Iterating over texts
## char text to sym morse
def char_to_sym(char_text):
    morse_code = ''
    for char in char_text:
        #check for spaces and add single space for every character and double for every word
        if char == ' ':
            morse_code += '  '
        else: 
            morse_code += CHARS_TO_SYM_MORSE[char.upper()] + ' '
    return morse_code

## sym morse to char text
def sym_to_char(morse_code):
    morse_code += ' '
    char_text = ''
  #char_word is for temporary holder to string letters into words
    char_word = ''
  #beep refers to dot, dash, or spaces
    for beep in morse_code:
      if (beep != ' '):
        i = 0
        char_word += beep
      else:
        i += 1
        if i == 2:
          char_text += ' '
        else:
          char_text += list(CHARS_TO_SYM_MORSE.keys())[list(CHARS_TO_SYM_MORSE.values()).index(char_word)]
          char_word = ''
    return char_text

# Setting up interface
def start_program():
    print("\n \n \n \n \n MORSE CODE GENERATOR AND DECODER.\n")
    interface = input("Would you like to generate or decode your morse code? Type '0' to generate a new morse code or '1' to decode your morse code. ")
    if interface == '0':
        char_text = input("Enter your message that your would like to encode: ")
        morse_code = char_to_sym(char_text)
        print(morse_code)
        if input("Would you like to decode your new morsed code? Type 'y' to decode. ").lower() == 'y':
            print(char_text)
            if input("Would you like to restart the program? Type 'y' to restart. ").lower() == 'y':
                start_program()
        else:
            start_program()
    elif interface == '1':
        morse_code = input("Enter your morse code that you would like to decode: ")
        char_text = sym_to_char(morse_code)
        print(char_text)
        if input("Would you like to return your text into morse code? Type 'y' to encode. ") == 'y':
            print(morse_code)
            if input("Would you like to restart the program? Type 'y' to restart. ").lower() == 'y':
                start_program()
        else:
            start_program()
    else:
        print("You have input an invalid code. \n")
        start_program()

start_program()
