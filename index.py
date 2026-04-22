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

#System

list = read_musics()
list_musics(list)





#menu de opcoes


#1. Adicionar musica
#2. Listar musicas
#3. Remover musica