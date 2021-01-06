#crio uma mensagem de boas vindas e imprimo

bem_vindo_msg = '''

Olá, nesse programa você poderá criar dois listas que serão posteriormente tratadas
pelo programa, sendo apresentadas suas saídas. Nesse formato:

PRIMEIRA LISTA: ----

SEGUNDA LISTA: ----

Os valores comuns às duas listas: ----
Os valores que só existem na primeira: ----
Os valores que existem apenas na segunda: ----
Uma lista com os elementos não repetidos das duas listas: ----
A primeira lista sem os elementos repetidos na segunda: ----

'''
print(bem_vindo_msg)

#defino os sets a serem comparados (não são indexados nem ordenados)
#usei o clear(), porque precisava adicionar um item para poder manipular o set e eu não queria que ele aparecesse na comparação. O clear() remove tudo e ainda me deixa manipular como um set
set_1 = {''}
set_1.clear()

set_2 = {''}
set_2.clear()

#parte que um usuário cria sua lista
#loop infinito com um break para a saída // a saída está antes da atribuição a fim de evitar a atribuição no caso de saída
print("Defina valores para a primeira lista (podem ser palavras, texto, números, etc). Para prosseguir escreva sair ou s\n")
while True:
    valor_do_ususario = ""
    valor_do_ususario = input("Escereva um valor para a lista: ")

    if valor_do_ususario.lower() == "sair" or valor_do_ususario.lower() == "s":
        break

    set_1.add(valor_do_ususario)
    print("\nlista do usuário: ", set_1, "\n")



print("Defina valores para a segunda lista (podem ser palavras, texto, números, etc). Para prosseguir escreva sair\n")
while True:
    valor_do_ususario = ""
    valor_do_ususario = input("Escereva um valor para a lista: ")

    if valor_do_ususario.lower() == "sair" or valor_do_ususario.lower() == "s":
        break

    set_2.add(valor_do_ususario)
    print("\nlista do usuário: ", set_2, "\n")
    


#se algum dos sets forem vazios, retorne a string "vazio" // é mais legível escrever "vazio" do que "set()"
def verify_set(set_for_check):
    if set_for_check == set():
        return "vazio"
    else:
        return set_for_check



#imprime os sets
print("\nPRIMEIRA LISTA: ", verify_set(set_1), end="\n\n")
print("SEGUNDA LISTA: ", verify_set(set_2), end="\n\n\n")


#aqui serão realizas as operações com o set_3 (sempre sendo alterado, dessa forma eu uso só ele e o set_4 quando necessário)
#estou usando funções prontas do python e que não alteram as originais, sempre retornando algo novo


#retorna um set com somente os elementos comuns no set_1 e set_2, a função intersection() retrona um novo set
set_3 = set_1.intersection(set_2)
print("Os valores comuns às duas listas: ", verify_set(set_3))


#retorno os sets juntos
set_3 = set_1.union(set_2)
#retorno o que é único no set_1, fazendo a diferença com o resultado anterior e com o set_2
set_3 = set_3.symmetric_difference(set_2)
print("Os valores que só existem na primeira: ", verify_set(set_3))


#retorno os sets juntos
set_3 = set_1.union(set_2)
#retorno o qué é único no set_2, fazendo a diferença com o resultado anterior e com o set_1
set_3 = set_3.symmetric_difference(set_1)
print("Os valores que existem apenas na segunda: ", verify_set(set_3))


#retorna um set com todos os elementos de set_1 e set_2 retirando as duplicatas, a função symmetric_difference() retrona um novo set com os elementos não repitidos
set_3 = set_1.symmetric_difference(set_2)
print("Uma lista com os elementos não repetidos das duas listas: ", verify_set(set_3))


#pego os itens em comum
set_3 = set_1.intersection(set_2)
#tiro a diferença, symmetric_difference() retorna um novo set com os itens que não são repitidos do primeiro set
set_4 = set_1.symmetric_difference(set_3)
print("A primeira lista sem os elementos repetidos na segunda: ", verify_set(set_4)) 

