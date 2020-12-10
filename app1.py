import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if(word in data):
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did u mean %s instead?"% get_close_matches(word,data.keys())[0])
        t=input("type y for yes or n for no........  ")
        if(t=='y'):
            return data[get_close_matches(word,data.keys())[0]]
        elif(t=='n'):
            return "check ur word again"
        else:
            return "type y or n... error occured"
    else:
        return "Word error"

word=input(" Enter word: ")
output=translate(word)

if type(output)==list:
    for i in output:
        print(i)
else:
    print(output)
