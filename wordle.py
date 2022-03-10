import csv
import random
import os
import platform

lang = ""
path = ""
word = ""

inPlace = "🟩"
aLetter = "🟨"
neither = "⬛"

choice  = ""

gameOver    = False
tries       = 0
cells, used = list(), list()
counts      = {}
verifier    = "🔵"
dialogs     = list()
dict = list()

for i in range(0, 6):
    cells.append([neither*5, ""])

# Do i really need to explain what this does?
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Gives all the variables its respective value according to the set language.
def loadFiles():
    global lang, path, dict, word, tries, cells, used, verifier, choice, dialogs
    with open('config', 'r') as config:
        reader = list(csv.reader(config, delimiter=","))[0]
        lang = reader[0]
        
    path     = "lang/" + lang

    dict.clear()
    csvDict  = csv.reader(open(f"{path}/usable.csv", 'r'))
    dict     = [word for sublist in csvDict for word in sublist]

    word     = random.choice(dict)
    tries    = 0
    used     = []
    verifier = "🔵"
    choice   = ""
    dialogs  = list()

    dict.clear()
    csvDict  = csv.reader(open(f"{path}/dict.csv", 'r'))
    dict     = [word for sublist in csvDict for word in sublist]

    csvDiags = list(csv.reader(open(f"{path}/dialogs.txt", 'r')))
    dialogs  = [sentence for sublist in csvDiags for sentence in sublist]
    
    for i in range(0, 6):
        cells[i] = [neither*5, ""]

loadFiles()

# Chekcs a given letter in a word the user typed for unnecesary duplicates.
def worthy(selected : str, word : str, count : int, letter : str):
    writtenAmount = selected.count(letter)
    realAmount    = word.count(letter)
    used          = 0
    toBeUsed      = 0

    if writtenAmount <= realAmount:
        return True
    
    else:
        for i in range(0, count):
            if selected[i] == letter:
                used += 1

        for i in range(count+1, 5):
            if selected[i] == word[i] == letter:
                toBeUsed += 1

        if used + toBeUsed < realAmount:
            return True

    return False

# Changes the language of the game.
def chLang():
    langs   = list()
    replace = ""

    for i in os.scandir("lang"):
        if i.is_dir():
            langs.append(i.name)

    clear()
    for i in range(0, len(langs)):
        print(f"{i+1}: {langs[i]}")

    new = input(dialogs[0])

    if new.isnumeric() and 0 <= int(new) - 1 < len(langs):
        replace = langs[int(new)-1]

        cfg = open("config", 'r')
        cfg = ''.join([i for i in cfg])

        cfg = cfg.replace(lang, replace)

        cfgNew = open("config", 'w')
        cfgNew.writelines(cfg)
        cfgNew.close()
        loadFiles()

    print(replace)

def pause():
    input(dialogs[4])

while not gameOver and tries < 6:
    clear()

    print(dialogs[1])
    
    for i in cells:
        print(f"{i[0]}\t{i[1]}")

    choice = input(f"\n{verifier}> ").upper()

    verifier = "🔴"

    if choice in dict and not choice in used:
        wordle   = ""
        verifier = "🟢"
        used.append(choice)

        for i in range(0, 5):
            if choice[i] == word[i]:
                wordle += inPlace

            elif choice[i] in word and worthy(choice, word, i, choice[i]):
                wordle += aLetter
            
            else:
                wordle += neither

        cells[tries] = [wordle, choice]
        tries += 1

    # Commands the user can type, like changing the language.
    elif choice[0] == '-':
        if choice == "-L":
            chLang()
            pause()
        elif choice == "-R":
            loadFiles()

    if choice == word:
        gameOver = True

clear()
for i in cells:
    print(f"{i[0]}\t{i[1]}")

if gameOver and tries <= 6:
    print(dialogs[2])
else:
    print(f"{dialogs[3]} {word}")
