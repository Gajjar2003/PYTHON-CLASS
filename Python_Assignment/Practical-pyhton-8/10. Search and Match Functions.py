# Write a Python program to search for a word in a string using re.search().

import re


text = "Python is a powerful programming language."


word = input("Enter the word to search: ")


result = re.search(word, text)

if result:
    print(f"✅ The word '{word}' is found in the string.")
else:
    print(f"❌ The word '{word}' is not found in the string.")


# Write a Python program to match a word in a string using re.match().

text = "Python is a powerful programming language."

word = input("Enter the word to match: ")


result = re.match(word, text)

if result:
    print(f"✅ The word '{word}' matches at the beginning of the string.")
else:
    print(f"❌ The word '{word}' does not match at the beginning of the string.")
