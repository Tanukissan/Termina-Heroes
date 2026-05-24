import random as rng
import os
import time as T

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def espera(segundos):
    T.sleep(segundos)

personagem={"ATK": rng.randint(1, 5),
            "DEF": rng.randint(1, 5), 
            "INT": rng.randint(1, 5), 
            "CHAR":rng.randint(1, 5), 
            "ESQ":5, 
            "HP":10, 
            "MP":10}

print("Seja bem-vindo ao Termina Heroes!" \
"\nVocê poderá se aventurar em um mundo de fantasia que existe dentro de seu terminal," \
"\nrepleto de monstros e eventos misteriosos..." \
"\nMas antes de adentrar nessa aventura, diga-me, qual é o seu nome?")

jogador = input("Digite o nome do personagem: ")

limpar()

print(f"Olá, {jogador}! Vamos começar a criar seu personagem." \
       "\nConfira os atributos do seu personagem logo abaixo:")

for atributo, valor in personagem.items():
    print(f"{atributo}: {valor}")

print("Gostaria de seguir com esses valores ou prefere alterar algum pelo sistema de pontos?" \
      "\n*No sistema de pontos você terá 10 pontos para distribuir "
      "\n(máx/5 p/ atributo)")
resposta = input("Seguir com estes atributos? (S/n): ")

if resposta.lower() == 'n':
    pontos = 10
    contador = 0
    limpar()
    print(f"Ótimo, {jogador}! Você tem {pontos}")

    for atributo in list(personagem.keys())[:4]:
        personagem[atributo] = int(input(f"{atributo}: "))
            
        if personagem[atributo] > 5 or personagem[atributo] < 1:
            print("Valor inválido! O valor deve ser entre 1 e 5.")
            personagem[atributo] = int(input(f"{atributo}: "))
        pontos -= personagem[atributo]

        if pontos < 0:
            print("Você excedeu o número de pontos disponíveis! Tente novamente.")
            pontos += personagem[atributo]
            personagem[atributo] = int(input(f"{atributo}: "))

        print(f"Pontos restantes: {pontos}")
        contador += 1

        if contador >= 4:
            break

print("Atributos finais do personagem:")
for atributo, valor in personagem.items():
    print(f"{atributo}: {valor}")

print(f"Ótimo, {jogador}! Agora que seu personagem está pronto, vamos começar a aventura!")

espera(4)
limpar()

