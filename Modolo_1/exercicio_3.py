# 3. Altere o código da atividade 1, criando uma variável divisor e, em seguida,
# verifique quais os números no intervalo entre 0 e 1000 (incluindo o 0 e
# excluindo o 1000) são múltiplos da variável divisor.

inicio = 0
fim = 1000
divisor = 75
for numero in range(inicio, fim):
    if numero % 75 == 0:
        print(numero)