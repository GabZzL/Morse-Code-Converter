# import the Translator class
from converter import Translator

# variable to run or not
is_running = True

# run multiple times
while is_running:
    # input to select the mode and insert the text
    mode = input('Text To Morse(T) or Morse To Text(M): ').lower()
    text = input('Please Insert Your Text: ').lower()

    # declare the converter object from the Translator class
    converter = Translator(text)

    # switch to run the different modes
    match mode:
        case 't':
            print('Text To Morse')
            print(converter.text_morse())
        case 'm':
            print('Morse To Text')
            print(converter.morse_text())
        case _:
            print('Error To Selected The Mode')

    # check if you want to run again
    answer = input('Do you want to run again? (y or n): ').lower()

    if answer == 'n':
        is_running = False
