#!/usr/bin/python3
import json
import difflib


global data_file

def definition(word):
    word=word.lower()
    if word in data_file:
        print(data_file[word])
    else:
        
        related=difflib.get_close_matches(word,data_file.keys(),n=4,cutoff=0.6)
        if len(related) > 0:
            print("The Entry did not match any word. Are you loooking for any of these?")
            print(related)
        else:
            print("Word not found")

if __name__=='__main__':
    with open('data.json') as fh:
        data_file=json.load(fh)
    word=input("Enter the word: ")
    definition(word)
