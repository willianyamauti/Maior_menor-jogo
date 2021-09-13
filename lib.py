from arte import logo, vs
from game_data import database
import random
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def escolher_aleatorio(database):
    opcao = random.choice(database)
    return opcao


def comparar_opcoes(escolha_jogador, segunda_opcao):
    fim_jogo = False
    if escolha_jogador['follower_count'] >= segunda_opcao['follower_count']:
        return fim_jogo
    else:
        fim_jogo = True
        return fim_jogo


def print_art(arte):
    print(arte)


def jogar_round(opcao_1, opcao_2):
    print(f"Compare A:{opcao_1['name']}, a {opcao_1['description']}, from {opcao_1['country']}")
    print_art(vs)
    print(f"Against B:{opcao_2['name']}, a {opcao_2['description']}, from {opcao_2['country']}")
    escolha = input("Who has more followers? Type A or B: ")
    while escolha.lower() != 'a' and escolha.lower() != 'b':
        escolha = input("Your choice is invalid, please choose between A ou B")
    if escolha.lower() == 'a':
        return comparar_opcoes(opcao_1, opcao_2), opcao_1
    else:
        return comparar_opcoes(opcao_2, opcao_1), opcao_2


