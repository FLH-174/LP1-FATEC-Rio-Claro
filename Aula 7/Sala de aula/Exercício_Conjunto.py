''' 
Considere o cenário:
A = set(list(range(1,10)))
B = set(list(range(5,15)))
C = set(list(range(9,20)))
#Qual o conjunto resultante:
a) A.intersection(B).intersection©
b) A.difference(C)
C) A.difference(C).intersection(B)

'''
A = set(list(range(1,10)))
B = set(list(range(5,15)))
C = set(list(range(9,20)))
print(A.intersection(B).intersection(C))
print(A.difference(C))
print(A.difference(C).intersection(B))