# 5. Crie um código que realize o somatório de todos os caracteres da seguinte
# string: numero = '127957'

numero = '127957'
soma = []
for n in numero:
    soma.append(int(n))

print(sum(soma))