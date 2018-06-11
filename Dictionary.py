
# Imports the standard library which lets you manipulate json objects
import json

# Loads the data into a python object - Python Dictionary
data = json.load(open("Resources/data.json"))
word = input("Enter a word: ")

if word in data.keys():
    listOfDef = data[word]
    for definition in listOfDef:
        print(definition)
else: print("No such word found")
