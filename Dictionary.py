
# Imports the standard library which lets you manipulate json objects
import json
import difflib
from difflib import SequenceMatcher

# Loads the data into a python object - Python Dictionary
data = json.load(open("Resources/data.json"))
word = input("Enter a word: ")

def printTranslations(w):
    listOfDef = data[w]
    for definition in listOfDef:
        print(definition)

def translate(w):
    w = w.lower()
    if w in data.keys():
        printTranslations(w)
    else:
        lista = difflib.get_close_matches(w,data.keys(),1,0.8)
        if lista:
            suggest = lista[0]
            answer = input("Did you mean: " + suggest + "  (y - yes || n -no)  ")
            if(answer == 'y'):
                printTranslations(suggest)
            else:
                print("Goodbye")
        else:
            print("Sorry, no word found")



translate(word)
