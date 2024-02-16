import random

def lista_embaralhada(numero):
    musicas = []
    for i in range(numero):
        nome_musica = input(f"digite o nome da musica {i + 1}: ")
        musicas.append(nome_musica)
    
    random.shuffle(musicas)

    return musicas

numero_musicas = int(input("digite a quantidade de musicas: "))
musicas = lista_embaralhada(numero_musicas)
print("lista de musicas embaralhadas:")
for i, musica in enumerate(musicas, start=1):
    print(f"{i} - {musica}")