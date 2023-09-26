# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random
from os import system, name

def limpa_tela():
    # windows
    if name == 'nt':
        _ = system('cls')
    # Mac e Linux
    else:
        _ = system('clear')

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe
class Hangman:

    # Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    # Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_palavra(self):
        rtn = ''

        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
            return rtn

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):

        print(board[len(self.letras_erradas)])
        print('\nPalavra: ' + self.hide_palavra())
        print('\nLetras erradas: ', )

        for letra in self.letras_escolhidas:
            print(letra,)
        print()
        print('Letras corretas: ',)

        for letra in self.letras_escolhidas:
            print(letra,)
        print()

# Método para ler palavra de forma aleatória
def rand_palavra():

    # lista de palavras
    palavras = ['morango', 'banana', 'uva', 'abacate', 'laranja']

    # escolhe aleatório
    palavra = random.choice(palavras)

    return palavra

def main():

    limpa_tela()

    # cria o objeto e seleciona uma palavra aleatória
    game = Hangman(rand_palavra())

    # enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz leitura do caracter
    while not game.hangman_over():
        # status
        game.print_game_status()

        #recebe input do terminal
        user_input = input('\nDigite uma letra: ')

        # verifica se a letra faz parte da palavra
        game.guess(user_input)

    # verifica status
    game.print_game_status()

    # de acordo com o status, imprime pro usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGAME OVER')
        print('A palavra era ' + game.palavra)


# executa o programa
if __name__ == '__main__':
    main()


