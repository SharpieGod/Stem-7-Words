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

total_length = sum(len(code) for code in morseCode.values())
average_length = total_length / len(morseCode)

print(f"Average Morse code length: {average_length}")

print(
    [
        tuple((list(morseCode.keys()).index(x), tuple((x, morseCode[x]))))
        for x in morseCode.keys()
    ]
)
