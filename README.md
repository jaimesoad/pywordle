# pywordle
---
## About

pywordle is a CLI implementation of the classic wordle.\
Essentially, you have six attemps to guess the correct 5-letter word before losing.

## Installation

Clone the repository and you're done.
```Bash
git clone https://github.com/jaimesoad/pywordle.git
```
Additionally, you can create a symlink of the bash script into your `.local/bin` directory, just make sure you've created it and it is on your `$PATH`:
```Bash
cd pywordle
chmod +x wordle #make it executable
ln -s wordle $HOME/.local/bin/wordle
```

## Usage

To play the game you can either type `python wordle.py`, `python3 wordle.py` or execute the bash script as `./wordle`.\
\
You can also use some commands inside the game:
- **Change the language:** `-l` or `-L`.
- **Reset the game:** `-r` or `-R`.

## Contribution

Right now, pywordle just supports English and Spanish, that's why I made it easy to add new languages.\
All you need to do is create a new folder inside the lang directory following the **ISO 639-1** code; basically the 2-letter code for each language. E.g: it is Italian, de is German, fr is French and so on.

After doing so, copy the list for all the 5-letter words (all caps) the player can use into a file called `dict.csv`, the list of words the player have to guess into a file called `usable.csv` and a txt with all the dialogs called `dialogs.txt` into your language directory.