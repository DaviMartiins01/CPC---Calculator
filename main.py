print("""
=====================================================================================
                              CALCULADORA CPC
=====================================================================================""")

print("Conjunção: ^ // Negação: ~ // Disjunção: v // Implicação: > // Bi-implicação: <")
print("-------------------------------------------------------------------------------------")
print("Obs: Não se esqueça dos parênteses.\n")

user_input = input("Informe a fórmula:")
list_of_atomic = []

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
for atomic in list_of_atomic:
    print("Vou ver isso dps")



number_of_rows = 2**len(list_of_atomic)

print(list_of_atomic)
print(number_of_rows)

