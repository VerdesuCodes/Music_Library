import json

def load_musics():
    with open("musics.json", "r", encoding="utf-8") as m:
        return json.load(m)
    
def list_musics(musics):
    for music in musics:
        print(music)

list = load_musics()
list_musics(list)





#menu de opcoes


#1. Adicionar musica
#2. Listar musicas
#3. Remover musica