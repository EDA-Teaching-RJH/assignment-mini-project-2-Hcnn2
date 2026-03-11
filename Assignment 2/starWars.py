# This is my Star Wars Force-Sensitive Beings Tracker.
# It tracks Jedi and Sith at the very start of ROTS.



import csv
import re



class ForceBeing:  # superclass
    def __init__(self, name, side, rank, midi, pid):
        self.name = name
        self.side = side
        self.rank = rank
        self.midi = midi
        self.pid = pid
    
    def get_info(self):
        return f"{self.name} ({self.side} - {self.rank}) | Midi: {self.midi} | ID: {self.pid}"

class LightBeing(ForceBeing):  # subclass with inheritance
    def __init__(self, name, rank, midi, pid):
        super().__init__(name, "Light", rank, midi, pid)
    
class DarkBeing(ForceBeing):  # second subclass
    def __init__(self, name, rank, midi, pid):
        super().__init__(name, "Dark", rank, midi, pid)



def init_database(): # Database of 5 light and 5 Dark side force beings (midis being midichlorian count)
    names = ["Obi-Wan Kenobi", "Anakin Skywalker", "Yoda", "Mace Windu", "Ahsoka Tano",
             "Darth Sidious", "Count Dooku", "Asajj Ventress", "General Grievous", "Darth Maul"]
    sides = ["Light", "Light", "Light", "Light", "Light",
             "Dark", "Dark", "Dark", "Dark", "Dark"]
    ranks = ["Jedi Master", "Jedi Knight", "Grand Master", "Jedi Master", "Padawan",
             "Emperor", "Sith Lord", "Sith Apprentice", "Sith Lord", "Sith Apprentice"]
    midis = [13500, 27700, 17500, 12000, 14000,
             20000, 14000, 11000, 5000, 12000]
    ids = ["FORCE-0001-L", "FORCE-0002-L", "FORCE-0003-L", "FORCE-0004-L", "FORCE-0005-L",
           "FORCE-0006-D", "FORCE-0007-D", "FORCE-0008-D", "FORCE-0009-D", "FORCE-0010-D"]
    return names, sides, ranks, midis, ids

def display_menu(current_user):
    print("     FORCE-SENSITIVE BEINGS TRACKER - ROTS")
    print("="*65)
    print(f"Logged in as: {current_user}")
    print("\n1. Add New Being")
    print("2. Remove Being")
    print("3. Update Rank")
    print("4. Display All Beings")
    print("5. Search Beings")
    print("6. Save to File")
    print("7. Load from File")
    print("8. Exit")
    print("-"*65)
    choice = input("Enter choice (1-8): ").strip()
    return choice



#File I/O 
def load_from_file(filename="force_beings.csv"):
    names = []
    sides = []
    ranks = []
    midis = []
    ids = []
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 5:
                    names.append(row[0])
                    sides.append(row[1])
                    ranks.append(row[2])
                    midis.append(int(row[3]))
                    ids.append(row[4])
        
        # If the file was empty or had no data, use the original 10 beings
        if len(names) == 0:
            raise FileNotFoundError
    except:
        print("No saved file yet - starting with 10 beings from ROTS.\nHint: Use \"Anakin Skywalker\" to enter\nSave to file as soon as you get in")
        return init_database()
    
    return names, sides, ranks, midis, ids

def save_to_file(names, sides, ranks, midis, ids, filename="force_beings.csv"):
    # Write all 5 lists to a csv file
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Side", "Rank", "Midichlorian", "ID"])
        for i in range(len(names)):
            writer.writerow([names[i], sides[i], ranks[i], midis[i], ids[i]])
    print("Roster saved to force_beings.csv!")



# Helper functions
def validate_force_id(pid):
    pattern = r"^FORCE-\d{4}-[LD]$"
    if re.fullmatch(pattern, pid):
        return True
    return False

def validate_midichlorian_count(count_str):
    if re.match(r'^\d{4,5}$', count_str):
        if int(count_str) >= 1000:
            return True
    return False

def flexible_search(term, name, side, pid):
    pattern = re.compile(term, re.IGNORECASE)
    if pattern.search(name) or pattern.search(side) or pattern.search(pid):
        return True
    return False

def is_valid_rank_for_side(rank, side):
    light_ranks = ["Padawan", "Jedi Knight", "Jedi Master", "Grand Master"]
    dark_ranks = ["Sith Apprentice", "Sith Lord", "Darth", "Emperor"]
    if side == "Light":
        return rank in light_ranks
    elif side == "Dark":
        return rank in dark_ranks
    return False



#Main feature functions
def add_being(names, sides, ranks, midis, ids):
    print("\n--- ADD NEW FORCE BEING ---")
    name = input("Full Name: ").strip().title()
    while True:
        side = input("Side (Light or Dark): ").strip().title()
        if side in ["Light", "Dark"]: break
        print("Only Light or Dark allowed.")
    
    valid_ranks = ["Padawan", "Jedi Knight", "Jedi Master", "Grand Master"] if side == "Light" else ["Sith Apprentice", "Sith Lord", "Darth", "Emperor"]
    while True:
        rank = input(f"Rank: ").strip().title()
        if rank in valid_ranks: break
        print("Invalid rank for this side.")
    
    while True:
        midi_str = input("Midichlorian Count: ").strip()
        if validate_midichlorian_count(midi_str):
            midi = int(midi_str)
            break
        print("Must be 4 or 5 digits and >= 1000.")
    
    while True:
        pid = input("ID (FORCE-0000-L/D): ").strip().upper()
        if validate_force_id(pid) and pid not in ids: break
        print("ID must be unique and correct format.")
    
    
    names.append(name)
    sides.append(side)
    ranks.append(rank)
    midis.append(midi)
    ids.append(pid)
    print(f" {name} added!")

def remove_being(names, sides, ranks, midis, ids):
    print("\n--- REMOVE BEING ---")
    pid = input("Enter ID: ").strip().upper()
    if pid in ids:
        idx = ids.index(pid)
        removed = names[idx]
        del names[idx]; del sides[idx]; del ranks[idx]; del midis[idx]; del ids[idx]
        print(f" {removed} removed.")
    else:
        print("ID not found.")

def update_rank(names, sides, ranks, ids):
    print("\n--- UPDATE RANK ---")
    pid = input("Enter ID: ").strip().upper()
    if pid in ids:
        idx = ids.index(pid)
        side = sides[idx]
        print(f"Current rank of {names[idx]}: {ranks[idx]}")
        
        if side == "Light":
            valid = ["Padawan", "Jedi Knight", "Jedi Master", "Grand Master"]
        else:
            valid = ["Sith Apprentice", "Sith Lord", "Darth", "Emperor"]
        
        while True:
            new_rank = input(f"New Rank (valid: {valid}): ").strip().title()
            if new_rank in valid:
                ranks[idx] = new_rank
                print("Rank updated.")
                break
            print("Invalid rank for this side.")
    else:
        print("ID not found.")

def display_all(names, sides, ranks, midis, ids):
    print("="*90)
    print("---All FORCE BEINGS---")
    print("="*90)
    print(f"{'ID':<12} {'Name':<22} {'Side':<8} {'Rank':<18} {'Midi':<10}")
    for i in range(len(names)):
        print(f"{ids[i]:<12} {names[i]:<22} {sides[i]:<8} {ranks[i]:<18} {midis[i]:<10}")
    print("="*90)

def search_being(names, sides, ranks, midis, ids):
    print("\n--- SEARCH ---")
    term = input("Search term: ").strip()
    found = False
    for i in range(len(names)):
        if flexible_search(term, names[i], sides[i], ids[i]):
            print(f"{ids[i]} | {names[i]} | {sides[i]} | {ranks[i]} | {midis[i]}")
            found = True
    if not found:
        print("No matches.")



def main():
    print("\n" + "="*65)
    print("     FORCE-SENSITIVE BEINGS TRACKER - ROTS")
    print("="*65)

    names, sides, ranks, midis, ids = load_from_file()

    # Only authorized users can enter, its not supposed to be designed for its security
    current_user = ""
    while True:
        entry = input("\nEnter your full name OR ID to log in: ").strip()
        found = False
        for i in range(len(names)):
            if entry.lower() == names[i].lower() or entry.upper() == ids[i]:
                current_user = names[i]
                found = True
                break
        if found:
            print(f"\nWelcome, {current_user}. May the force be with you.")
            break
        else:
            print("Not recognized in the archives. Try again.")

    while True:
        choice = display_menu(current_user)
        
        if choice == "1":
            add_being(names, sides, ranks, midis, ids)
        elif choice == "2":
            remove_being(names, sides, ranks, midis, ids)
        elif choice == "3":
            update_rank(names, sides, ranks, ids)
        elif choice == "4":
            display_all(names, sides, ranks, midis, ids)
        elif choice == "5":
            search_being(names, sides, ranks, midis, ids)
        elif choice == "6":
            save_to_file(names, sides, ranks, midis, ids)
        elif choice == "7":
            names, sides, ranks, midis, ids = load_from_file()
            print("Roster reloaded from file.")
        elif choice == "8":
            print("\nMay the force be with you.")
            break
        else:
            print("Invalid choice. Try 1-8.")

if __name__ == "__main__":
    main()