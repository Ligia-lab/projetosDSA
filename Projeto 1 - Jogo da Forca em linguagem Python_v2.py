import random
from os import system, name


# função pra limpar a tela a cada execução
def limpa_tela():
    # windows
    if name == 'nt':
        _ = system('cls')

    # Mac e Linux
    else:
        _ = system('clear')


# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]


# função
def game():

    limpa_tela()

    print('\nJOGO DA FORCA!!')
    print('Advinhe a palavra:\n')

    # lista de palavras
    lista = ['banana', 'abacate', 'uva', 'morango', 'laranja', 'manga', 'tomate']

    # escolhe palavra
    palavra = random.choice(lista)

    # tracinhos
    letras_descobertas = ['_' for letra in palavra]

    # tentativas
    chances = 6

    # erros
    letras_erradas = []

    # loop de tentativas
    while chances > 0:

        print(display_hangman(chances))

        print(' '.join(letras_descobertas))
        print('\nTentativas restantes: ', chances)
        print('Letras erradas: ', ' '.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()

        # condicional, verificação das letras na palavra
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1

        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # VITÓRIA
        if '_' not in letras_descobertas:
            print('\nVocê venceu!!! A palavra era: ', palavra)
            break

    # DERROTA
    if '_' in letras_descobertas:
        print('\nVocê perdeu, a palavra era: ', palavra)


# bloco main
if __name__ == '__main__':
    game()
    print('\nVocê jogou forca em Python! :)')








