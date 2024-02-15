import random
import os
def getsingleword():
    with open("word.txt","r") as word:
        wordlist = word.readlines()
        impword = wordlist[random.randint(0,len(wordlist)-1)]
        pureword = impword.split('\n')
        return pureword[0]


word = getsingleword()
print(word)

def wordsapace(l):
    for i in range(len(l)):
        print(l[i], end=" ")
    print()

def hangman(trice):
    print()
    arr = [
        [" ", " ", "o"],
        ["\n", "--"], ["|"],["--","\n"],
        [" ", " ", "|"],
        ["\n", " ", "/"],
        [" ", "\\"],
        [""]

    ]

    for i in range(trice):
        for j in range(len(arr[i])):
            print(arr[i][j], end="")

word = getsingleword()
trice = 0
chance = 8
g = set()
l = ["_" for i in range(len(word))]
wordsapace(l)
hangman(trice)

while trice != chance:
    if word.upper() == ''.join(l):
        print("\nwoooohhh...... I am going to live ")
        break
    print("guess the word?")
    guess = input("\nwhat could be the next letter ? ")

    os.system("cls")
    g.add(guess)
    if len(g) > 0:
        for i in g:
            print("(", end="")
            print(i, end="")
            print(")", end="")
    print("\n")

    if guess in word:
        index = [i for i,l in enumerate(word) if l==guess]
        for i in index:
            l[i] = guess.upper()

    hangman(trice)
    print()
    print()
    wordsapace(l)

    if guess not in word:
        trice += 1
        hangman(trice)
        print()
        print()
        wordsapace(l)
else:
    print("\nI trusted you...")
    print(f"The word was, {word}.")