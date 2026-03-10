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

