import random
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Lists of races, classes, and their traits
races = {
    "Human": {
        "Traits": ["Versatile", "Extra Language"],
        "Ability Bonus": {"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1},
    },
    "Elf": {
        "Traits": ["Darkvision", "Fey Ancestry", "Trance"],
        "Ability Bonus": {"Dexterity": 2, "Intelligence": 1},
    },
    "Dwarf": {
        "Traits": ["Darkvision", "Dwarven Resilience", "Tool Proficiency"],
        "Ability Bonus": {"Constitution": 2, "Wisdom": 1},
    },
    "Halfling": {
        "Traits": ["Lucky", "Brave", "Halfling Nimbleness"],
        "Ability Bonus": {"Dexterity": 2, "Charisma": 1},
    },
    "Dragonborn": {
        "Traits": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"],
        "Ability Bonus": {"Strength": 2, "Charisma": 1},
    },
    "Gnome": {
        "Traits": ["Darkvision", "Gnome Cunning", "Artificer’s Lore"],
        "Ability Bonus": {"Intelligence": 2, "Dexterity": 1},
    },
    "Half-Elf": {
        "Traits": ["Fey Ancestry", "Skill Versatility"],
        "Ability Bonus": {"Charisma": 2, "Choose 2 others": 1},
    },
    "Half-Orc": {
        "Traits": ["Darkvision", "Menacing", "Relentless Endurance"],
        "Ability Bonus": {"Strength": 2, "Constitution": 1},
    },
    "Tiefling": {
        "Traits": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
        "Ability Bonus": {"Charisma": 2, "Intelligence": 1},
    },
}

classes = {
    "Artificer": {
        "Hit Die": "1d8",
        "Primary Ability": "Intelligence",
        "Skills": ["Arcana", "History"]
    },
    "Barbarian": {
        "Hit Die": "1d12",
        "Primary Ability": "Strength",
        "Skills": ["Animal Handling", "Intimidation"]
    },
    "Bard": {
        "Hit Die": "1d8",
        "Primary Ability": "Charisma",
        "Skills": ["Performance", "Persuasion"]
    },
    "Cleric": {
        "Hit Die": "1d8",
        "Primary Ability": "Wisdom",
        "Skills": ["Religion", "Insight"]
    },
    "Druid": {
        "Hit Die": "1d8",
        "Primary Ability": "Wisdom",
        "Skills": ["Nature", "Animal Handling"]
    },
    "Fighter": {
        "Hit Die": "1d10",
        "Primary Ability": "Strength or Dexterity",
        "Skills": ["Athletics", "Acrobatics", "Survival"]
    },
    "Monk": {
        "Hit Die": "1d8",
        "Primary Ability": "Dexterity or Wisdom",
        "Skills": ["Acrobatics", "Religion"]
    },
    "Paladin": {
        "Hit Die": "1d10",
        "Primary Ability": "Strength or Charisma",
        "Skills": ["Athletics", "Religion"]
    },
    "Ranger": {
        "Hit Die": "1d10",
        "Primary Ability": "Dexterity or Wisdom",
        "Skills": ["Survival", "Perception"]
    },
    "Rogue": {
        "Hit Die": "1d8",
        "Primary Ability": "Dexterity",
        "Skills": ["Stealth", "Deception", "Sleight of Hand"]
    },
    "Sorcerer": {
        "Hit Die": "1d6",
        "Primary Ability": "Charisma",
        "Skills": ["Arcana", "Deception"]
    },
    "Warlock": {
        "Hit Die": "1d8",
        "Primary Ability": "Charisma",
        "Skills": ["Arcana", "History"]
    },
    "Wizard": {
        "Hit Die": "1d6",
        "Primary Ability": "Intelligence",
        "Skills": ["Arcana", "History"]
    }
}


# Function to roll ability scores (standard 4d6 drop the lowest)
def roll_ability_scores():
    scores = []
    for _ in range(6):  # Generate 6 ability scores
        roll = sorted([random.randint(1, 6) for _ in range(4)])[1:]  # Drop the lowest
        scores.append(sum(roll))  # Sum the three highest
    return {
        "Strength": scores[0],
        "Dexterity": scores[1],
        "Constitution": scores[2],
        "Intelligence": scores[3],
        "Wisdom": scores[4],
        "Charisma": scores[5],
    }

# Function to generate a random name
def generate_name():
    first_names = {
        "Human": ["Adrian", "Alaric", "Althea", "Anastasia", "Anders", "Anya", "Arianna", "Aveline", "Balthazar", "Beatrice", 
            "Benjamin", "Briar", "Camille", "Cassandra", "Cecilia", "Charles", "Cyrus", "Dahlia", "Darius", "Elena", 
            "Emery", "Evelyn", "Finnian", "Gabriel", "Gideon", "Hannah", "Isadora", "Jasper", "Juliet", "Katherine", 
            "Leander", "Lysandra", "Matthias", "Mira", "Nathanael", "Octavia", "Ophelia", "Orion", "Peregrine", "Rhiannon", 
            "Sabrina", "Sebastian", "Selene", "Tobias", "Ulysses", "Vesper", "Wesley", "Zara", "Alden", "Anwen", 
            "Archer", "Athena", "Briar", "Briony", "Cassian", "Clara", "Cyrus", "Dahlia", "Delilah", "Desmond", 
            "Dorian", "Elise", "Fiona", "Gwendolyn", "Ivy", "Julian", "Kael", "Kira", "Landon", "Luna", 
            "Margaret", "Maximilian", "Niamh", "Orlaith", "Ronan", "Sabine", "Soren", "Sylvia", "Thalia", "Violet", 
            "Wren", "Aurelia", "Branwen", "Calista", "Caspian", "Daphne", "Emrys", "Galen", "Isolde", "Jasmine", 
            "Leona", "Marius", "Nadia", "Phaedra", "Rhiard", "Rosalind", "Sable", "Tamsin", "Viggo", "Yara"],
        
        "Elf": ["Thalindra", "Elrond", "Faelar", "Aelene", "Lirael", "Isilwen", "Elandor", "Nimrodel", 
                "Arannis", "Caelum", "Lyrian", "Aerendyl", "Caladwen", "Maelon", "Thalion", "Nymwen", "Aelar", 
                "Syril", "Vandor", "Faylinn", "Yavanna", "Cyrdane", "Faeloria", "Elandril", "Luthien", "Galanthir", 
                "Aldaron", "Elowen", "Sylphira", "Cyndor", "Velenar", "Ithilwen", "Siltharion", "Talarian", "Ariandel", 
                "Vaelora", "Zyra", "Elunara", "Nimara", "Ythril", "Olyndra", "Selendil", "Lirael", "Finael", "Anarion", 
                "Aesthir", "Illyndor", "Cynthera", "Seraphiel", "Eryndor", "Thirion", "Calenwen", "Lindoriel", "Vaelion", 
                "Zindel", "Myrdion", "Vilya", "Elenion", "Theryn", "Faelwyn", "Galadrieth", "Elenaria", "Aelion", "Nymriel", 
                "Cyrwen", "Felorin", "Sylwen", "Ithralis", "Thaliondor", "Nerithil", "Ilmarel", "Zyther", "Aelthir", "Syndra", 
                "Elandoriel", "Aeloria", "Celebrian", "Thalyn", "Nimrael", "Isilthir", "Elrin", "Calendir", "Lyren", "Dathir", 
                "Vanyarin", "Elorindel", "Cyndal", "Therindor", "Nithrin", "Ilarion", "Nysil", "Faelthir", "Mithlond", "Eryndil", 
                "Elwen", "Thalarion", "Sylthia", "Vaelwyn", "Aerendyl", "Lilyth", "Tharindor", "Elara", "Rhyldan", "Maelwen", 
                "Cylyndor", "Vandoriel", "Ardil", "Aelwen", "Isiliel", "Yavriel", "Fynel", "Galindra", "Zyldra", "Cyndoriel", 
                "Illyndra", "Arianel", "Elunara", "Thalionel", "Sylareth"],
        
        "Dwarf": ["Thorin", "Gimli", "Dwalin", "Balin", "Kili", "Fili", "Oin", "Gloin", "Bofur", "Bifur", "Bombur", "Durin", 
                  "Dain", "Nori", "Ori", "Ferdinand", "Thrain", "Thrain", "Krag", "Bergin", "Rurik", "Keldorn", "Ulgar", 
                  "Gorim", "Balgar", "Brunhild", "Torgar", "Duggan", "Nimral", "Ragnar", "Korrin", "Mordrin", "Frothgar", 
                  "Alaric", "Varric", "Garnok", "Grimnar", "Orin", "Eldrin", "Madrin", "Korgrim", "Thulgar", "Fargrim", "Darrin", 
                  "Gorath", "Kharim", "Brungrin", "Othgar", "Barin", "Murnin"],
        
        "Halfling": ["Alton", "Beren", "Cade", "Dorian", "Eldon", "Fendrel", "Gorbin", "Hob", "Iggy", "Jasper", "Kellen", 
                     "Lenny", "Milo", "Nim", "Ollie", "Pippin", "Quinn", "Rudy", "Samwise", "Tansy", "Udo", "Vince", 
                     "Wendel", "Xander", "Yarrow", "Zee", "Bran", "Clover", "Daisy", "Ella", "Fiona", "Gwen", "Hazel", "Ivy", 
                     "Juniper", "Kira", "Lila", "Maggie", "Nora", "Opal", "Peony", "Rosie", "Sage", "Tilly", "Violet", "Willow"],
        
        "Dragonborn": ["Balasar", "Kriv", "Geryn", "Sora", "Zyphor", "Thurvok", "Vythar", "Raxith", "Nimrath", "Shyrak", 
                    "Xilthar", "Drakkon", "Tyrak", "Sareth", "Zarvok", "Vexis", "Raegarn", "Krothar", "Jorvath", 
                    "Pyrax", "Zyra", "Rhalak", "Draxan", "Gorath", "Kryntor", "Tharak", "Zorith", "Harkoth", 
                    "Vurak", "Draughar", "Nythar", "Chyrax", "Kzarnak", "Xarath", "Yzorn", "Trakar", "Ghrond", 
                    "Thorin", "Varnok", "Isharn", "Braxith", "Drakthar", "Lazrak", "Syrath", "Cyndrath", 
                    "Rhaegar", "Zarok", "Gorzhak", "Kethar", "Valkar", "Zerath", "Gryndor", "Fyrak", "Nerith", 
                    "Vethrin", "Jorath", "Krylar", "Zythorn", "Drazhar", "Salthar", "Krivaan", "Ryzhak", "Tyrvok"],
        
        "Gnome": ["Fizban", "Zook", "Nim", "Quinn", "Tink", "Pip", "Sprocket", "Wizzle", "Nackle", "Bimble", 
                "Glum", "Fiddle", "Boggle", "Jingle", "Wiggle", "Dabble", "Gimble", "Cogs", "Pippin", 
                "Zippy", "Sprig", "Razzle", "Bibble", "Tinkers", "Sprock", "Whimsy", "Fizzle", "Mumble", 
                "Jubbly", "Blinky", "Fumble", "Wizzlefizz", "Knickknack", "Snicker", "Tweak", "Nimble", 
                "Flimflam", "Whizzle", "Bumble", "Puddle", "Cuddle", "Wobble", "Tiddle", "Snappy", 
                "Doodle", "Jink", "Fuzzle", "Blinky", "Glint", "Bumblefluff", "Tinkerbell", "Corky"],
        
        "Half-Elf": ["Lyra", "Elandra", "Kira", "Draven", "Aelar", "Virelia", "Thalion", "Cyril", "Nymira", "Caelum", 
                "Illyana", "Rhyne", "Elysia", "Fenrin", "Seraphine", "Alyndra", "Elion", "Kellan", "Thalindra", 
                "Zyra", "Lirael", "Elowen", "Riven", "Faelar", "Cyndra", "Galen", "Tarian", "Aranel", 
                "Kyrian", "Vaelora", "Lunara", "Fendrel", "Syris", "Caelum", "Althaea", "Drael", "Raelan", 
                "Vareth", "Amara", "Zyphor", "Ilyana", "Nyx", "Thandor", "Vaelin", "Dorian", "Nimue", 
                "Aelwen", "Zylen", "Talia", "Mirelle", "Elion", "Calen", "Xandria", "Rhiannon"],
        
        "Half-Orc": ["Grom", "Sharn", "Rok", "Draug", "Thok", "Garak", "Zug", "Krag", "Tarn", "Brak", 
                "Uruk", "Gor", "Hark", "Drok", "Zar", "Morg", "Thul", "Gash", "Kragor", "Rash", 
                "Vark", "Brok", "Grond", "Krath", "Duk", "Torg", "Skar", "Ogar", "Vok", 
                "Rond", "Nok", "Tug", "Zog", "Zarok", "Gorthak", "Rhul", "Grommash", "Thoknor", 
                "Zarn", "Drokthar", "Ragnar", "Ulthak", "Grim", "Jorr", "Drogath", "Krul", 
                "Skarn", "Mok", "Rogar", "Vroth", "Tharok", "Morr", "Hrak", "Zyrok"],
        
        "Tiefling": ["Zariel", "Astaroth", "Lilith", "Kallista", "Malakar", "Nerith", "Riven", "Zephyra", 
                "Lucian", "Sorath", "Vesper", "Draziel", "Kethrys", "Xandria", "Thalor", "Nyx", 
                "Zypher", "Mordred", "Inara", "Varyn", "Rhaziel", "Selene", "Thorne", "Caelum", 
                "Aerith", "Zyra", "Nimue", "Valen", "Dusk", "Ravyn", "Talon", "Arion", 
                "Vael", "Jezebel", "Zelthar", "Malachi", "Dorian", "Elysia", "Khalas", "Rhyne", 
                "Vespera", "Dante", "Erevan", "Kaelith", "Azazel", "Lyra", "Fenris", "Kallian"],
    }

    race = random.choice(list(first_names.keys()))
    first_name = random.choice(first_names[race])
    last_names = ["the Bold", "the Swift", "the Brave", "the Wise", "the Shadow", "the Bright", "the Fierce", 
                "the Strong", "the Wily", "the Cunning", "the Unseen", "the Just", "the Fearless", 
                "the Quick", "the Daring", "the Mighty", "the Silent", "the Clever", "the Fierce", 
                "the Stalwart", "the Gallant", "the Shining", "the Boldheart", "the Vigilant", 
                "the Eternal", "the Dreamer", "the Hunter", "the Storm", "the Seeker", "the Wandering", 
                "the Graceful", "the Wild", "the Guardian", "the Eternal", "the Protector", "the Flame", 
                "the Moonlit", "the Earthshaker", "the Swiftfoot", "the Radiant", "the Eternal", 
                "the Shadowstalker", "the Ironfist", "the Swiftblade", "the Nightingale", "the Thundering"
]
    return f"{first_name} {random.choice(last_names)}", race

# Function to generate a random character
def generate_character():
    name, race = generate_name()
    character_class = random.choice(list(classes.keys()))
    ability_scores = roll_ability_scores()

    character = {
        "Name": name,
        "Race": race,
        "Class": character_class,
        "Traits": races[race]["Traits"],
        "Hit Die": classes[character_class]["Hit Die"],
        "Primary Ability": classes[character_class]["Primary Ability"],
        "Ability Scores": ability_scores,
    }

    return character

# Function to display the character in the text box
def display_character():
    character = generate_character()
    output_text.delete(1.0, tk.END)  # Clear previous text
    output_text.insert(tk.END, f"Name: {character['Name']}\n")
    output_text.insert(tk.END, f"Race: {character['Race']}\n")
    output_text.insert(tk.END, f"Class: {character['Class']}\n")
    output_text.insert(tk.END, f"Traits: {', '.join(character['Traits'])}\n")
    output_text.insert(tk.END, f"Hit Die: {character['Hit Die']}\n")
    output_text.insert(tk.END, f"Primary Ability: {character['Primary Ability']}\n")
    output_text.insert(tk.END, "Ability Scores:\n")
    for ability, score in character['Ability Scores'].items():
        output_text.insert(tk.END, f"  {ability}: {score}\n")

# Create the main window
root = tk.Tk()
root.title("D&D Character Generator")

# Create a button to generate the character
generate_button = tk.Button(root, text="Generate Character", command=display_character)
generate_button.pack(pady=10)

# Create a scrolled text box to display the character
output_text = scrolledtext.ScrolledText(root, width=40, height=20, wrap=tk.WORD)
output_text.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
