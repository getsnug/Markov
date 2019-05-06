#this file cleans up the text, by removing book and author titles, along with the -Jane Doe, class of 2020 at the end of every rec
txt = open(r"train.txt", "r+")
prevDash = False
cleanedArr = []
#checks if there is a - and removes that line and the next
for line in txt:
    if("\x80\x94" in line):
        prevDash = True
    elif(prevDash==True):
        prevDash = False
        pass
    else:
        cleanedArr.append(line)
print(cleanedArr)
txtC = open(r"cleaned.txt", "a")
#Writes cleaned text to a file named cleaned.txt, only needs to be run once.
for elem in cleanedArr:
    txtC.write(elem)
