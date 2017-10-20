#!/usr/bin/python3
import json
global data_file

def definition(word):
    try:
        print(data_file[word])
    except:
        print("Word not found")

if __name__=='__main__':
    with open('data.json') as fh:
        data_file=json.load(fh)
    word=input("Enter the word: ")
    definition(word)
