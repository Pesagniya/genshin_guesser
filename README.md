# Guess the Character: Genshin Impact

A simple Python command-line game where you guess characters from hints. Each round provides a few hints about a character, and you have to guess who it is.

---

## Features

- Randomly selects a character from a JSON dataset.
- Provides 3 hints per round (among weapon, attribute, element and affiliation).

## Requirements

- Python 3.x
- `characters.json` file with character data (use update_list.py for latest list of characters):

```json
[
  {
    "name": "Amber",
    "element": "Pyro",
    "weapon": "Bow",
    "nation": "Mondstadt",
    "affiliation": "Knights of Favonius"
  },
]
```

## Installation
Requirements: Python installed and an IDE like Visual Studio Code.

1. Clone this repository

```bash
git clone https://github.com/Pesagniya/genshin_guesser.git
```

2. Navigate to its directory

3. Run the game by running
```bash
python main.py
```

## Credits
Character data is fetched using [this API](https://github.com/genshindev/api?tab=readme-ov-file)
