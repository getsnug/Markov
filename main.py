#This file generates the markov chain and saves it to the text file gen.txt
import random
myString = open("cleaned.txt", "r")
myString = myString.read()
words = myString.split()
words.reverse()
wordArrA = {}
i = 0
prevWord = "\n"
#The following for loop is supposed to fix an issue with ' and " but it doesn't currently work
for word in words:
    if "\xe2\x80\x99t" in word:
        word.replace("\xe2\x80\x99t", "'")
    if "\xe2\x80\x9d" in word:
        word.replace("\xe2\x80\x9d", '"')
    try:
        wordArrA[word].append(prevWord)
        prevWord = word
    except KeyError:
        wordArrA[word] = [prevWord]
        prevWord = word
print(wordArrA)


genString = open("gen.txt", "a")
currWord = " "
sentences = 0
#The following while loops go through and generate the text, the first one makes sure that the generated text starts with an uppercase letter. There is also a repitition of this so that all new sentences start with an uppercase letter.
while currWord[0].lower() == currWord[0]:
    currWord = random.choice(wordArrA.keys())
while sentences<5:
    genString.write(currWord + " ")
    if('.' in currWord):
        sentences+=1
        #Makes sure that sentences start with upper case
        while currWord[0].lower() == currWord[0]:
            currWord = random.choice(wordArrA.keys())
    else:
        currWord = random.choice(wordArrA[currWord])

