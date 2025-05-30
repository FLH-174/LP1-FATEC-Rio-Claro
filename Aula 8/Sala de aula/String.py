# Strings são sequancias imutaváis de pontos de códigos Unicode

nome = "Ana"
idade = (40)
mensagem = f"Olá {nome}, sua idade: {idade} anos"
print(mensagem)

# Métodos para String

len(mensagem) #Quantidade de itens na string, neste caso 'mensagem'

S = "Fatec Rio Claro"
S.startswith # Letra que começa a string (Resposta é True or False)
S.endswith # Letra que termina a string (Resposta é True or False)

in # Para verificar se algo está na string (Resposta é True or False)

# count - Verifica quantas vezes a cadeia de caractéries é encontrada na string
S = "um trige, dois tigres, três tigres" 
S.count('tigre') 
S.count('tigres')
S.count('tigre, 11')

# find - Verifica em que ocorrencia começa a sequência de caracteres
S = "um tigre, dois tigres, três tigres"
S.find('trige')
S.find('tigre, 10')

# Centraliza a string na descrição da resposta
S="FATEC"
"X" + S.center(20,'.') + "X"

S.split # Quebra a string grande em menores

S.replace

s.is

S.upper # Converte todos os caracteres para maiúsculos
S.lower # Converte todos os caracteres para minúsculos