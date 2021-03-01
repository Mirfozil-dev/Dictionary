from difflib import get_close_matches
import json

data = json.load(open("data.json"))
start = "y"


def translate(word):
    query = ""  # Result which we get from our data.json
    result = ""  # Total result

    # Checking for string format
    if word.lower() in data:
        result = word.lower() + ": "
        query = data[word.lower()]
    elif word.title() in data:
        result = word.title() + ": "
        query = data[word.title()]
    elif word.capitalize() in data:
        result = word.capitalize() + ": "
        query = data[word.capitalize()]
    elif word.upper() in data:
        result = word.upper() + ": "
        query = data[word.upper()]
    # Checking for close matches
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean: %s instead" % get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no: ").lower()
        if decide == "y":
            result = get_close_matches(word, data.keys())[0] + ": "
            query = data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return "Sorry, this word doesn't exist in our dictionary!"
        else:
            return "You have entered wrong input!"
    # If there it no any words in dictionary
    else:
        query = "Sorry, this word doesn't exist in our dictionary!"
    # Checking if there are more than one definitions of the word
    if type(query) == list:
        for item in query:
            result = result + item + "\n"
    else:
        result = result + query
    # Returning overall result
    return result


while start == "y":
    word = input("Enter the word you want to search: ")

    output = translate(word)

    print(output)

    start = input("Enter y if you want to translate again or n to stop application: ").lower()
else:
    print("GoodBye!")
