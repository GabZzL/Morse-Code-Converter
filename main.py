# import the Translator class
from converter import Translator

# input to select the mode and insert the text
mode = input('Morse To Text(M) or Text To Morse(T): ').lower()
text = input('Please Insert Your Text: ').lower()

# declare the converter object from the Translator class
converter = Translator(text)

# switch to run the different modes
match mode:
    case 'm':
        print('Text To Morse')
        print(converter.text_morse())
    case 't':
        print('Morse To Text')
        print(converter.morse_text())
    case _:
        print('Error To Selected The Mode')
