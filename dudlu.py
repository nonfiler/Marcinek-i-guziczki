import enchant
 
# Create an instance of the English dictionary
english_dict = enchant.Dict("en_US")

# Get user input
user_input = input("Enter a word: ")

# Check if the word is valid English
if english_dict.check(user_input):
    print("Valid English word!")
else:
    print("Not a valid English word.")

# Get suggestions for a misspelled word
# misspelled_word = "helo"
# suggestions = english_dict.suggest(misspelled_word)
# print("Suggestions:", suggestions)