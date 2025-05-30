# Faça um programa que percorra duas listas e gere uma terceira lista sem elementos repetidos
# Listas iniciais
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

# Combinar as duas listas
lista_combinada = lista1 + lista2

# Criar uma lista sem elementos repetidos
lista_sem_repetidos = list(set(lista_combinada))

# Exibir o resultado
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista sem elementos repetidos:", lista_sem_repetidos)

# Outra maneira de descrever a lista sem repetição
Lista1=[1,2,3,4,5,6,7,8,9]
Lista2=[5,6,7,8,9,10,11,12,13,14,15]

Lista3=[]
for item in Lista1:
    if not item in Lista3:
       Lista3.append(item)

for item in Lista2:
    if not item in Lista3:
        Lista3.append(item)
print (Lista3)