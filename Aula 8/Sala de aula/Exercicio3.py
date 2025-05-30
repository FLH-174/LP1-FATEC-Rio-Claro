"""
Solicite uma frase ao usuário e pergunte por uma palavra a ser procurada.
Informe se a palavra existe na frase e, se existir, em qual posição ela aparece pela primeira vez.
"""

frase = input("Digite uma frase")
if frase.find('passaros'):
print('passaros voando')
else:
    print('gaiolas são um crime')