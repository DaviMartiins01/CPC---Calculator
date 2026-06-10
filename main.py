print("""
=====================================================================================
                              CALCULADORA CPC
=====================================================================================""")

print("Conjunção: ^ // Negação: ~ // Disjunção: v // Implicação: > // Bi-implicação: <")
print("-------------------------------------------------------------------------------------")
print("Obs: Não se esqueça dos parênteses.\n")

user_input = input("Informe a fórmula:")
list_of_atomic = []

#Só pega s fórmulas atômicas e coloca numa lista
for char in user_input:
    if char == "^":
        continue
    elif char == "~":
        continue
    elif char == "v":
        continue
    elif char == ">":
        continue
    elif char == "<":
        continue
    elif char == "(":
        continue
    elif char == ")":
        continue
    else:
        list_of_atomic.append(char)


atomics = []

#Tira as fórmulas atômicas repetidas
for atomic in list_of_atomic:
    number_of_comparison = 0
    #Se não tem nada dentro da lista de fórmulas atômicas não repetidas. Coloca.
    if not atomics:
        atomics.append(atomic)
    else:
        #Tendo algo dentro ele passa a comparar se o item da list_of_atomics já está dentro da atomics.
        for index in range(len(atomics)):
            #Checa se os itens são diferentes.
            if atomics[index] != atomic:
                #aumenta a contagem de diferenças
                number_of_comparison += 1
                #Se a contagem de diferença for igual ao tamanho da lista significa que o item de list_of_atomics
                #É diferente a todos os itens da lista atomics
                #Então adiciona esse item da list_of_atomic a lista atomics.
                if number_of_comparison == len(atomics):
                    atomics.append(atomic)

number_of_rows = 2**len(atomics)

print(f"Resultado que eu quero: {atomics}")
print(f"Número de linhas: {number_of_rows}")

