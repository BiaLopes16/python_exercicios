# Criando a lista "numeros" com os números de 1 a 10
numeros = list(range(1, 11))

# Criando a lista "dobro" que contém o dobro de cada número da lista "numeros"
dobro = [num * 2 for num in numeros]

# Imprimindo as duas listas
print("Lista 'numeros':", numeros)
print("Lista 'dobro':", dobro)
