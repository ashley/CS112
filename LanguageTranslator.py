morseAlphabet ={
    "A" : ".-",
    "B" : "-...",
    "C" : "-.-.",
    "D" : "-..",
    "E" : ".",
    "F" : "..-.",
    "G" : "--.",
    "H" : "....",
    "I" : "..",
    "J" : ".---",
    "K" : "-.-",
    "L" : ".-..",
    "M" : "--",
    "N" : "-.",
    "O" : "---",
    "P" : ".--.",
    "Q" : "--.-",
    "R" : ".-.",
    "S" : "...",
    "T" : "-",
    "U" : "..-",
    "V" : "...-",
    "W" : ".--",
    "X" : "-..-",
    "Y" : "-.--",
    "Z" : "--..",
    " " : "/",
    "." : "STOP",
    "," : ",",
    "?" : "QUESTION",
    "'" : "'"
    }

file = open('banana.txt') #Opens the file
words = (file.readlines()[0]) #Puts the joke onto a str called words
file.close()
#print(words)

print(''.join(morseAlphabet[i] for i in words.upper())) #coverts each word to uppercase then to morse, join, print




