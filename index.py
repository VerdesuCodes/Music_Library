import json

#Conection functions (Write and Read)
def read_musics():
    with open("musics.json", "r", encoding="utf-8") as m:
        return json.load(m)
    
def write_musics(musics):
    with open("musics.json", "w", encoding="utf-8") as m:
        json.dump(musics, m, ensure_ascii=False, indent=2)

#Other functions

def list_musics(musics):
    for music in musics:
        print(music)

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

list = read_musics()
while True:
    print("Your list of musics: \n")
    list_musics(list)
    option = input("\nOptions: \n1. Add music\n2. Remove music\n3. Exit\n")

    if option == "1":
        add_music(list)

    if option == "2":
        remove_music(list)

    if option == "3":
        print("Exiting...")
        break






#menu de opcoes


#1. Adicionar musica
#2. Listar musicas
#3. Remover musica