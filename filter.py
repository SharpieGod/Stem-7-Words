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

with open("originalWords.txt", "r") as f:
    words = f.read().upper().splitlines()

validWords = []
for word in words:
    if sum([len(morseCode[x]) for x in word]) == 13:
        validWords.append(word)

with open("filteredWords.txt", "w") as f:
    f.write("\n".join(validWords))
