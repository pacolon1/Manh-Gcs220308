from library_item import LibraryItem

# Update library items to include the mp3_file argument
library = {}
library["01"] = LibraryItem("NoLoveNoLife", "HIEUTHUHAI", 4, "Spring", "BloomingPoison.mp3")
library["02"] = LibraryItem("Exit Sign", "HIEUTHUHAI", 5, "Autumn", "Magic.mp3")
library["03"] = LibraryItem("TOKYO cypher", "LilWuyn", 3, "Spring", "Ra.mp3")
library["04"] = LibraryItem("1-800-LOVE", "HIEUTHUHAI", 5, "Winter", "Nerves.mp3")
library["05"] = LibraryItem("Vinflow", "Wxrdie", 3, "Summer", "Aura.mp3")
library["06"] = LibraryItem("Banh Mi Khong", "DatG", 4, "Winter", "Pinocchio.mp3")
library["07"] = LibraryItem("Ve Ben Anh", "J97", 1, "Autumn", "BadTrip.mp3")

def list_all():
    output = ""
    for key, item in library.items():
        output += f"{key} {item.info()}\n"
    return output

def get_name(key):
    if key in library:
        return library[key].name
    return None

def get_singer(key):
    if key in library:
        return library[key].singer
    return None

def get_season(key):
    if key in library:
        return library[key].season
    return None

def get_rating(key):
    if key in library:
        return library[key].rating
    return -1

def set_rating(key, rating):
    if key in library:
        library[key].rating = rating

def get_play_count(key):
    if key in library:
        return library[key].play_count
    return -1

def increment_play_count(key):
    if key in library:
        library[key].play_count += 1

def play(key):
    if key in library:
        library[key].play_count += 1

def reset_play_count(key):
    if key in library:
        library[key].play_count = 0

def get_mp3_file(key):
    if key in library:
        return library[key].mp3_file
    return None
