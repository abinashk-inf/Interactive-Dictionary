#!/usr/bin/python3
import json
global data_file

def definition(word):
    print(data_file[word])
    

if __name__=='__main__':
    with open('data.json') as fh:
        data_file=json.load(fh)
    word=input("Enter the word: ")
    definition(word)
