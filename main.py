import json
import random

DATA_FILE = "characters.json"

# Attributes we can use as hints
HINT_ATTRIBUTES = ["element", "weapon", "nation", "affiliation"]


def load_characters():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_random_character(characters):
    return random.choice(characters)


def get_random_hints(character):
     # Weapon is mandatory
    mandatory = ["weapon"]
    others = [attr for attr in HINT_ATTRIBUTES]

    # Pick 2 random extra hints
    extra_hints = random.sample(others, 2)

    selected = mandatory + extra_hints

    return [f"{attr.capitalize()}: {character[attr]}" for attr in selected]

def play_round(characters):
    character = get_random_character(characters)
    hints = get_random_hints(character)

    print("\n=== A mysterious figure stands before you. Here's what you know: ===")
    for h in hints:
        print(" •", h)

    guess = input("\nWho is this character? ").strip().lower()
    correct = character["name"].lower()

    if guess == correct:
        print("✔ Correct!")
    else:
        print(f"✘ Wrong. The character was **{character['name']}**.")


def main():
    print("Please be advised that only full names are accepted.")
    print("Loading character data...")
    characters = load_characters()

    while True:
        play_round(characters)
        again = input("\nPlay again? (y/n) ").strip().lower()
        if again != "y":
            break

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
