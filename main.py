import string
print("Welcome To This Palindrome Recognition System")
word = input("Enter a phrase or a word: ")
def ip(blah):   
    blah = blah.lower()
    blah = blah.replace(" ", "")
    if blah == blah[::-1]:
        return blah[::-1]
if ip(word):
    print(word, 'is a palindrome!')
else:
    print(word, 'is not a palindrome')
while True:
    word = input("Enter a phrase or a word: ")
    if ip(word): 
        print(word, 'is a palindrome!')
    else:
        print(word, 'is not a palindrome.')