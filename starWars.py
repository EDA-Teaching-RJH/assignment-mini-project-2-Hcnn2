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
    print("4. Display Full Roster")
    print("5. Search Beings")
    print("6. Save to File")
    print("7. Load from File")
    print("8. Calculate Total Midichlorians")
    print("9. Exit")
    print("-"*65)
    choice = input("Enter choice (1-9): ").strip()
    return choice

def main():
    print("\n" + "="*65)
    print("     FORCE-SENSITIVE BEINGS TRACKER - ROTS")
    print("="*65)

    # AUTHENTICATION - only authorized users
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
