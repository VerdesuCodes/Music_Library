import json
import unicodedata

#Conection functions (Write and Read)
def read_musics():
    with open("musics.json", "r", encoding="utf-8") as m:
        return json.load(m)
    
def write_musics(musics):
    with open("musics.json", "w", encoding="utf-8") as m:
        json.dump(musics, m, ensure_ascii=False, indent=2)

#Other functions
def remove_accents(text):
    return ''.join(
        c for c in unicodedata.normalize('NFD', text) 
        if unicodedata.category(c) != 'Mn')

def list_musics(musics):
    musics.sort(key=lambda m: remove_accents(m).lower())
    current_Letter = ""
    if not musics:
        print("No music registered.")
        return
    for music in musics:
        first_Letter = remove_accents(music[0]).upper()
        if first_Letter != current_Letter:
            current_Letter = first_Letter
            print(f"\n--- {current_Letter} ---")
        print(music)
    count = len(musics)
    print(f"\n---------\nTotal: {count} music{'s' if count != 1 else ''}.")

def add_music(musics):
    name = input("Write the name of the music: ")

    if name == "":
        print("Invalid name.")
        return

    if name in musics:
        print("This music already exists!")
        return
    
    if name.lower() == "exit":
        return

    musics.append(name)
    write_musics(musics)

def remove_music(musics):
    name = input("Write the name of the music to remove: ")

    if name in musics:
        musics.remove(name)
        write_musics(musics)
    else:
        print("This music insn't in the list!")

#System
musics = read_musics()

while True:
    option = input("\nOptions: \n1. See all musics \n2. Add music\n3. Remove music\n4. Exit\n")

    if option == "1":
        print("Your list of musics: \n")
        list_musics(musics)
    
    if option == "2":
        add_music(musics)   
        
    elif option == "3":
        remove_music(musics)

    elif option == "4":
        print("Exiting...")
        break

    else:
        print("Invalid option, try again.")

# Quero adicionar uma parte de quando acecar a lista ele saia do menu, e apenas quando clicar exit retorne