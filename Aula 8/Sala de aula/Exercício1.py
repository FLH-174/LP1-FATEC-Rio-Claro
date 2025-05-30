"""
Escreva um programa que leia uma frase do usuário e diga quantas vezes a palavra "Python"
aparece na frase, independentemente de ser maiúscula ou minúscula.

"""
frase = "O Python é um bom programa para iniciantes, pois o Python é uma programação superior"

minusculo = frase.lower()
print(minusculo)

maiusculo = frase.upper()
print(maiusculo)

print(frase.count('Python'))
