import random as r

with open("filteredWords.txt", "r") as f:
    words = f.read().upper().splitlines()
with open("usedWords.txt", "r") as f:
    usedWords = f.read().upper().splitlines()
    words = [x for x in words if x not in usedWords]

randomWord = r.choice(words)

print(f"Random word is: {randomWord}")
usedWords.append(randomWord)

with open("usedWords.txt", "w") as f:
    f.write("\n".join(usedWords))
