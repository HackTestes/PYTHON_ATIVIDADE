
#defino uma mensagem de boas vindas
def bem_vindo():

    #crio uma variável com uma mensagem de boas vindas explicando o programa e imprimo na tela
    msg_boas_vindas = '''

    Esse programa é um jogo da velha.
    As linhas e colunas começam a partir de 1 a vão até 3 (exemplo: linha 1 e coluna 1)

        1-1  1-2  1-3
        2-1  2-2  2-3
        3-1  3-2  3-3

    Divirta-se!!!

    '''
    print(msg_boas_vindas, end="\n\n\n")

#crio uma matriz representando os espaços do jogo da velha // ele vai servir principalmente para poder referenciar as coordenadas com mais facilidade
#cada item da lista possui uma outra lista dentro
tabela_jogo = [

    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]

]


#defino uma função para imprimir o jogo na tela
def imprimir_jogo():

    #pula duas linha no começo da impressão
    print("\n\n")
    #acessa a linha int(tabela_jogo)
    for linha in range(len(tabela_jogo)): #o range() cria um objeto com uma lista de números que começa no zero e o len() pega o tamanho

        #acessa cada coluna ou item
        for coluna in range(len(tabela_jogo[linha])):
            #imprime cada item individualmente // \t - tab // "   " - espaço entre itens // end="" - não pule de linha
            print("\t", tabela_jogo[linha][coluna], "   ", end="")

        #ao terminar a linha da tabela pule uma linha na tela
        print("\n")

    #ao terminar a tabela pule 2 linhas
    print("\n\n")
    

#crio contadores para determinar o vencedor // acabei criando-as como variáveis globais (achei mais fácil de manipular assim)
contador_X = 0
contador_O = 0
contador_espacos_cheios = 0


#defino uma função para determinar um vencedor ou a impossibilidade de um (quando dá velha)
def vencedor_ou_velha():
    
    #defino uma função que reinicializa os contadores, caso contrário iriam incrementar incorretamente, quebrando as condições
    def reinicializa_contador():
        global contador_X, contador_O, contador_espacos_cheios #o global serve para acessar variáveis globais e como os contadores são globais,ou seja, serve para acessá-los
        contador_X = 0
        contador_O = 0
        contador_espacos_cheios = 0

    #essa função verifica os contadores. Se houver vencedor: imprima uma mensagem e termine o programa. Se ninguém ganhar, só reinicie os contadores
    def verifica():
        global contador_X, contador_O, contador_espacos_cheios
        if contador_X == 3:
            print("\nO jogador X ganhou!")
            raise SystemExit #gera em "erro" que executa a saída do programa

        elif contador_O == 3:
            print("\nO jogador O ganhou!")
            raise SystemExit

        elif contador_espacos_cheios == 9:
            print("\nDeu velha!")
            raise SystemExit
            
        else:
            reinicializa_contador() #chama a função

    #essa função verifica linha por linha no jogo incrementando os contadores de "X" ou "O"
    def vencedor_linha():
        global contador_X, contador_O, contador_espacos_cheios
        #acessa a linha
        for linha in range(len(tabela_jogo)):

            #acessa os itens da linha
            for item in range(len(tabela_jogo[linha])):

                if tabela_jogo[linha][item] == "X":
                    contador_X = contador_X + 1

                elif tabela_jogo[linha][item] == "O":
                    contador_O = contador_O + 1
                
            verifica() #chama a função de verificar, deve ser feita a cada linha para manter os contadores corretos e poder fazer a verificação correta


    #mesma a coisa que o da linha, mas esse verifica cada coluna
    def vencedor_coluna():
        global contador_X, contador_O, contador_espacos_cheios
        for coluna in range(len(tabela_jogo[0])): #descobre quantas colunas tem (itens na linhas), como é 3x3 posso usar qualquer linha

            for item in range(len(tabela_jogo)): #acessa os itens de cada coluna

                if tabela_jogo[item][coluna] == "X":
                    contador_X = contador_X + 1

                elif tabela_jogo[item][coluna] == "O":
                    contador_O = contador_O + 1
                
            verifica()#mesmo princípio de antes

    #esse verifica vencedores na diagonal
    def vencedor_diagonal():
        global contador_X, contador_O, contador_espacos_cheios

        #variável que decresce para a diagonal crescente
        j = 2

        #diagonal decrescente
        #como só tem 3 e as coordenadas são repitidas (1-1,2-2,3-3), cheguei nisso: um loop que repete 3 vezes e a variável i é igual nas coordenadas
        for i in range(3):
            if tabela_jogo[i][i] == "X":
                contador_X = contador_X + 1

            elif tabela_jogo[i][i] == "O":
                contador_O = contador_O + 1

        verifica() #só verifica depois de "olhar" toda a diagonal

        #diagonal crescente
        #mesma coisa de antes, mas dessa vez uma das coordenadas começava no máximo valor possível e decrementava em 1 a cada mudança de posição
        for i in range(3):
            
            if tabela_jogo[i][j] == "X":
                contador_X = contador_X + 1

            elif tabela_jogo[i][j] == "O":
                contador_O = contador_O + 1

            j = j - 1 #sempre decrementa a cada loop

        verifica()

    #esse verifica a impossibilidade de vencedores ("Deu velha!")
    #basicamente funciona assim: se ninguém ganhar o jogo -> ele é executado (se alguém ganhar a finalização é realizada antes) -> se todas as posições estiverem ocupadas (e como o programa não foi finalizado) --
    #--> só podemos concluir que ninguém ganhou e que não existem mais jogadas possíveis -> "DEU VELHA!"
    def velha():
        global contador_X, contador_O, contador_espacos_cheios
        #acessa linha
        for linha in range(len(tabela_jogo)):

            #acessa o item
            for item in range(len(tabela_jogo[linha])):

                if tabela_jogo[linha][item] == "X" or tabela_jogo[linha][item] == "O": #identifica se a posição está preenchida ou não
                    contador_espacos_cheios = contador_espacos_cheios + 1
                
        verifica() #so verifica depois de "olhar" todo o jogo

    #aqui são cahamdas as funções dentro do verifica() na ordem que eu quero a execução
    vencedor_linha()
    vencedor_coluna()
    vencedor_diagonal()
    velha() #está no final para garantir que o programa não dê velha mesmo tendo um vencedor
        
        
#defino uma função que mostra qual é o jogador da vez(recebendo como um argumento) e escerve a jogada
def escrever_vez(jogada_vez):
    #variável que recebe as corrdenadas em formato de string para poder usar a função split() do python
    coord_str = ""

    #loop infinito
    while True:

        #tratamento de erro
        try:
            coord_str = input("Escreva as a linha e coluna que você deseja escrever " + jogada_vez + " (nessa ordem e separado por espaço): ") #imprime a mensagen de jogada
            coord_list = coord_str.split() #separa a string em uma lista para acessar a lista tabela_jogo

            #tranforma os itens em inteiros // tranforma os itens da lista de strings em inteiros para poderem ser usados
            for i in range(len(coord_list)):
                coord_list[i] = int(coord_list[i]) - 1 #erro gera um ValueError

            if len(coord_list) != 2: #se o usuário não der a quantidade exata de coordenadas gere um erro
                raise Exception()

        #mensagem de tratamento de erro
        except ValueError:
            print("\nEntrada de dados inválida! Tente novamente com apenas números separados por espaço\n")
        except Exception:
            print("\nVocê não passou cooredenadas suficientes ou passou muitas\n")
        
        #não tendo erros, avalie se a posição não está ocupada para prosseguir(break)
        else:
            if tabela_jogo[coord_list[0]] [coord_list[1]] == "_":
                break
            else:
                print("\nEspaço já ocupado! Escolha outra coordenada\n")

    tabela_jogo[coord_list[0]] [coord_list[1]] = jogada_vez #escreve a jogada na tabela_jogo


#defino uma função com todas as funções principais para a jogo
def func_vez(var_vez):
    escrever_vez(var_vez)
    imprimir_jogo()
    vencedor_ou_velha()


#defino uma main() que será chamada para a execução do programa // ela exibe a mensagem de boas vindas, o jogo inicial // depois chama a func_vez() passando como a vez(argumento) as strings "X" e "O"
def main():
    bem_vindo()
    imprimir_jogo()

    while True:
        func_vez("X")

        func_vez("O")

#função main é chamada
main()