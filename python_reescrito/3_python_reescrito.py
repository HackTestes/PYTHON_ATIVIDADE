#crio uma mensagem de boas vindas e imprimo

msg_boas_vindas = '''

Nesse programa você escolherá dois números, em seguida o programa mostrará
o maior número entre os dois e se o primeiro é múltiplo do segundo, usando
dois algoritmos diferentes.

Observação: para usar números decimais utilize o ponto, ao invés da vírgula.

'''
print(msg_boas_vindas)

#inicio as variáveis
var_1 = 0
var_2 = 0
var_resultado = 0

#input(mensagem) mandar um mensagem para o usuário e esperar uma entrada, float() transforma a entrada em um float
#loop infinito com tratamento de erro
while True:
    try:
        var_1 = float(input("Escolha o seu primeiro número \n"))
        var_2 = float(input("Escolha o seu segundo número \n"))
    except:
        print("Valor inválido! Tente novamente com um número \n\n")
    else:
        break

#crio uma função com def e dou um nome
def maior_num():
    #uso a função do python que mostra o maior numero (max())
    var_resultado = max(var_1, var_2)
    print("\nEscreva uma função que retorne o maior de dois números :", var_resultado, end="\n\n") 


def multiplo_whi():
    #se uma das variaveis for 0 não execute esse bloco
    if var_1 or var_2 != 0:
        #inicializa variavel de controle
        i = 0
        #inicializa var_resultado como var_1
        var_resultado = var_1
        #quantas vezes multiplicar a var_2 para chegar a var_1 ou próximo?
        while i < var_1 // var_2:
            var_resultado = var_resultado - var_2
            i = i + 1

        #verificar resultados
        if var_resultado == 0:
             print("WHILE - Verdadeiro, o primeiro é multiplo do segundo", end="\n\n")
        if 0 != var_resultado:
            print("WHILE - Flaso, o primeiro não é multiplo do segundo", end="\n\n")
        
        
        #ao sair do loop, verificar novamente (pois ele pode sair normalmente), e então retornar falso
        


#utiliza o operador % que retorna o resto, dessa forma se o resto não for 0, ele não é multiplo do segundo
def multiplo_extra():
    if 0 == var_1 % var_2:
        print("EXTRA - Verdadeiro, o primeiro é multiplo do segundo", end="\n\n")
    else:
        print("EXTRA - Flaso, o primeiro não é multiplo do segundo", end="\n\n")

#define uma main() com todas as funções
def main():
    maior_num()
    multiplo_whi()
    multiplo_extra()

#todas as funções são chamadas
main()




