#!/usr/bin/python3
import json
import difflib


global data_file

def definition(word):
    if word in data_file:
        content=data_file[word]
        for meanings in content:
            print(meanings)
    elif word.lower() in data_file:
        content=data_file[word.lower()]
        for meanings in content:
            print(meanings)
    else:       
        related=difflib.get_close_matches(word,data_file.keys(),3,0.7)
        if len(related) > 0:
            print("The Entry did not match any word. Are you loooking for any of these?")
            for r in related:
                print(r)
        else:
            print("Word not found")

if __name__=='__main__':
    with open('data.json') as fh:
        data_file=json.load(fh)
    word=input("Enter the word: ")
    definition(word)
