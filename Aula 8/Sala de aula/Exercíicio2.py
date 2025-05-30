"""
Peça ao usuário para digitar uma frase. Verifique se:
1- A frase começa com "Bom dia"
2- A frase termina com "obrigado"
Mostre mensagens diferentes dependendo do resultado
"""


frase = input('Digite a frase: ')

if frase.startswith('Bom dia'):
    print('A frase começa com "Bom dia"')
elif frase.endswith('obrigado'):
    print('A frase termina com "obrigado"')
else:
    print('Sua frase não começa com bom dia ou termina com obrigado')
