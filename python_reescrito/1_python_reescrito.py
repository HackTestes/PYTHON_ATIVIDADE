

#DEFinindo uma função de boas vindas, nela é impresso na tela uma mensagem infromando sobre o programa
def bem_vindo():
    #atribuo uma mensagem multilinha a uma variável e depois imprime
    mensagem_bem_vindo = '''
    Olá, nesse programa você pode imprimir uma tabuada baseado no valor e operação escolhidos.
    Para escolher uma operação você poderá escrever o nome dela exatamente, nome sem acentos, só as primeiras 4 letras,
    utilizar os símbolos indicados ou ainda o número indicado no menu. 
    A operação especial SAIR termina a execução do programa.

    Observação: os números escolhidos são transformados em inteiros! Além disso, os nomes de operações podem ser
    escritos tanto em caixa alta ou baixa.

    A tabuada começa em zero e termina em dez, apresentando a seguinte estrutura:
    
    OPERAÇÃO: ----
    VALOR INTEIRO ESCOLHIDO: ----
    0: *resultado*
    1: *resultado*
    ...
    ...
    ...
    10: *resultado*
    '''
    print(mensagem_bem_vindo)


#aqui são definidas as funções das operações; eles mostram a operação escolhida, o valor selecionado pelo usuário e a tabuada
#como todas possuem o mesmo modelo (ele mudam apenas a mensagem de operação e o operador para o cálculo), comentarei apenas a primeira função

def op_adicao(num_do_usuario):
    #imprime a operação e o valor escolhido (o \n serve para pular ma linha)
    print("OPERAÇÃO: ADIÇÃO \nVALOR INTEIRO ESCOLHIDO: ", num_do_usuario, end="\n")
    #loop FOR: para valores em(in) algo faça X // o range(num) cria um espécie de lista com números necessários para o loop - ele começa em 0 e vai até o num escolhido menos 1
    #range(4) - 0, 1, 2, 3
    for valor in range(11):
        #realiza a operação e imprime a tabuada
        print(valor, ": ", valor + num_do_usuario, end="\n")

def op_subtracao(num_do_usuario):
    print("OPERAÇÃO: SUBTRAÇÃO \nVALOR INTEIRO ESCOLHIDO: ", num_do_usuario, end="\n")
    for valor in range(11):
        print(valor, ": ", valor - num_do_usuario, end="\n")

def op_multiplicacao(num_do_usuario):
    print("OPERAÇÃO: MULTIPLICAÇÃO \nVALOR INTEIRO ESCOLHIDO: ", num_do_usuario, end="\n")
    for valor in range(11):
        print(valor, ": ", valor * num_do_usuario, end="\n")

def op_divisao(num_do_usuario):
    print("OPERAÇÃO: DIVISÃO \nVALOR INTEIRO ESCOLHIDO: ", num_do_usuario, end="\n")
    for valor in range(11):
        print(valor, ": ", valor / num_do_usuario, end="\n")


#defino uma função para o usuário selecionar uma operação e um valor, além de executá-la
def usuario_seleciona_executa():
    
    #crio uma string multilinha e atribuo a uma variável
    menu = '''

    Menu de operações:

    ADIÇÃO(1) (+)
    SUBTRAÇÃO(2) (-)
    MULTIPLICAÇÃO(3) (*)
    DIVISÃO(4) (/)
    
    SAIR(5) (..)

    '''
    #crio um dicionário para guardar as funções (mais precisamente para selecioná-las)
    #um dicionário funciona com uma chave : valor, ele é bem semelhante a uma atribuição normal de variáveis
    #para atribuir uma função, o nome da função deve ser usado sem os parênteses e quando chamar a chave use os parênteses
    #nome_da_chave: nome_da_func --> nome_da_chave()
    #OBS: existem outras formas de usar as funções, essa é apenas uma delas
    dic_de_op = {

        "1": op_adicao,
        "+": op_adicao,
        "adição": op_adicao,
        "adicao": op_adicao,
        "adic": op_adicao,

        "2": op_subtracao,
        "-": op_subtracao,
        "subtração": op_subtracao,
        "subtracao":op_subtracao,
        "subt": op_subtracao,

        "3": op_multiplicacao,
        "*": op_multiplicacao,
        "multiplicação": op_multiplicacao,
        "multiplicacao": op_multiplicacao,
        "mult": op_multiplicacao,

        "4": op_divisao,
        "/": op_divisao,
        "divisão": op_divisao,
        "divisao": op_divisao,
        "divi": op_divisao,

        #essas aqui servem para apenas mostrarem que existem, dessa forma dão positivo quando são chamadas
        #e para retronam uma string para realizar a saída
        "5": "sair",
        "..": "sair",
        "sair": "sair"

        
    }

    #defino uma função que imprime uma mensagem de erro
    def msg_invalido():
        print("Operação inválida! Tente novamente", end="\n\n")

    #loop infinito até que o usuário selecione a saída
    while True:

        #imprime o menu
        print(menu)

        #outro loop infinito, esse é para a seleção de uma operação
        while True:
            #tratamento de erro
            #se uma operação for VÁLIDA, OCORRERÁ um ERRO (por não passarmos argumentos)
            #se a opção SAIR for selecionada, ela será encontrada no dicionário > mas como é uma chamada de função > OCORRERÁ um ERRO (não é possível chamar strings)
            #se a opção for INVÁLIDA, NÃO OCORRERÁ um ERRO > apenas a opção INVÁLIDA não causa ERRO
            #dessa forma, na ocorrência de ERRO(uma operação VÁLIDA) > saia do loop (break)

            #Por que fiz essa lógica inversa? Eu não queria executar as funções de operação, dessa forma eles causam um erro ao tentar
            try:
                op_do_usuario = input("Selecione uma operação do menu: ") #recebe uma string do usuário
                op_do_usuario = op_do_usuario.lower() #tranforma a string em caixa baixa, dessa forma o usuário pode escrever do jeito que quiser (alta ou baixa)
                dic_de_op.get(op_do_usuario, msg_invalido)() #chama uma das chaves e realiza uma chamada de função - dic_de_op.get(executa_se_tem_no_dicionário, executa_se_não_tem_no_dicionário)
            except:
                break

        #se a op_do_usuário for de saída, realize a saída 
        if dic_de_op.get(op_do_usuario) == "sair": 
            break

        #necessita de tratmento de erro para entradas incorretas
        while True:
            #trata o erro, caso o valor passado não possa ser transformado em um inteiro
            try:
                num_do_usuario_escolhido = int(input("Selecione um número para realizar a operação: ")) #recebe uma string e transforma em inteiro
                print("\n")
            except ValueError:
                print("Entrada inválida! Tente novamente com um número inteiro\n\n") #caso o erro ValueError ocorra faça isso
            else:
                break #caso não tenha erro, saia do loop

        #chama a operação correspondente no dicionário e passa como argumento o num_do_usuário
        dic_de_op.get(op_do_usuario, msg_invalido)(num_do_usuario_escolhido)

#define uma função main() contendo todas as funções principais do programa
#caso o usuário termine a usuario_seleciona_executa(), é impresso uma mensagem mostrando a saída
def main():
    bem_vindo()
    usuario_seleciona_executa()
    print("Saída executada!")

#função main é chamada
main()
