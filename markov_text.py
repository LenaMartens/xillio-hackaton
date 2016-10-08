import json
import os

import markovify
import sys


def train():
    for root, dirs, files in os.walk("messages/"):
        for file in files:
            # Get raw text as string.
            with open("messages/"+file) as f:
                text = f.read()

            # Build the model.
            if text != "":
                try:
                    text_model = markovify.Text(text)
                    extension = os.path.splitext(file)[0]
                    print(extension)
                    write_file = open("models/" + extension + ".json", 'w')
                    json.dump(text_model.chain.to_json(), write_file)
                except IndexError:
                    pass


def generate(extension):
    text_model = json.load(open("models/"+extension+".json"))
    model = markovify.Text.from_chain(text_model)
    print(model.make_short_sentence(120, tries=1000))


'''
filter on None and @
'''

if __name__ == "__main__":
    extension = sys.argv[1]
    generate(extension)


