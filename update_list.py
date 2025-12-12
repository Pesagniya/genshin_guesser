import requests
import json

API_LIST = "https://genshin.jmp.blue/characters"
API_CHARACTER = "https://genshin.jmp.blue/characters/{}?lang=en"
OUTPUT_FILE = "characters.json"

def fetch_character_data(char_id):
    url = API_CHARACTER.format(char_id)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"[!] Skipped {char_id}")
        return None

    data = response.json()

    return {
        "id": char_id,
        "name": data.get("name", "Unknown"),
        "element": data.get("vision", "Unknown"),
        "weapon": data.get("weapon", "Unknown"),
        "nation": data.get("nation", "Unknown"),
        "affiliation": data.get("affiliation", "Unknown"),
    }


def fetch_all_characters():

    characters = []

    for char in requests.get(API_LIST).json():
        print(f"[*] Fetching: {char}...")
        info = fetch_character_data(char)
        if info:
            characters.append(info)

    return characters


def save_data(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"\n[✔] Saved {len(data)} characters → {OUTPUT_FILE}")


if __name__ == "__main__":
    print("=== Updating Genshin Character List ===")
    data = fetch_all_characters()
    save_data(data)
