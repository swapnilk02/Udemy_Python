# programme to check if the word is palindrome or not....i.e the word and its reverser are same or not ?
def is_palindrome(string):
    return string[::-1].casefold()==string.casefold()


word=input("please enter a word to check: ")

if is_palindrome(word):
    print("word is palindrome")
else:
    print("word is not palindrome")