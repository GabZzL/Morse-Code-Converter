# json library
import json

# open the json files
with open(file='text-morse.json', mode='r') as data:
    text_morse = json.load(data)

with open(file='morse-text.json', mode='r') as data:
    morse_text = json.load(data)


# Translator class, functions to convert
class Translator:
    def __init__(self, input_text):
        self.text = input_text
        self.converted_text = ''
        self.text_to_morse = text_morse
        self.morse_to_text = morse_text

    # text to morse
    def text_morse(self):
        for letter in self.text:
            try:
                new_letter = self.text_to_morse[letter]
            except KeyError:
                new_letter = '/'
            finally:
                self.converted_text += f' {new_letter}'

        return self.converted_text

    # morse to text
    def morse_text(self):
        morse_input = self.text
        morse_list = morse_input.split()

        for code in morse_list:
            try:
                new_letter = self.morse_to_text[code]
            except KeyError:
                new_letter = ' '
            finally:
                self.converted_text += new_letter

        return self.converted_text
