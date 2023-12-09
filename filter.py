morseCode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
}

wordLength = input("Word length: ")
morseCodeLength = input("Morse code length: ")

words = []
with open("allWords.txt", "r") as f:
    words = [x for x in f.read().upper().splitlines() if len(x) == int(wordLength)]

validWords = []

for word in words:
    if sum([len(morseCode[x]) for x in word]) == int(morseCodeLength):
        validWords.append(word)

print(*validWords, sep="\n")
