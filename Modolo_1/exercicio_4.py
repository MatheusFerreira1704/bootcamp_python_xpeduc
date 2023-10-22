# 4. Crie um código declarando as seguintes variáveis do tipo string:
# # variáveis do tipo string
# nome = 'João da Silva'
# cidade = 'São Paulo'
# cpf = '123.456.789-00'
# Em seguida, realize as seguintes transformações nas variáveis:
# ● Transforme todos os caracteres das variáveis em maiúsculo;
# ● Transforme todos os caracteres das variáveis em minúsculo;
# ● Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
# ● Exiba o número de caracteres de cada variável;
# ● Remova os pontos (.) e o hífen (–) da variável cpf.


# variáveis do tipo string
nome = 'João da Silva'
cidade = 'São Paulo'
cpf = '123.456.789-00'

#Transforme todos os caracteres das variáveis em maiúsculo;
print(f"{nome.upper()}, {cidade.upper()}")
print()
#Transforme todos os caracteres das variáveis em minúsculo;
print(f"{nome.lower()}, {cidade.lower()}")
print()
#Exiba a posição do caractere ã, se presente, em cada uma das variáveis;
print(f"Nome fica na posição: {nome.find('ã')}, \n Cidade fica na posição: {cidade.find('ã')} ")
print()
#Exiba o número de caracteres de cada variável;
print(f"Nome tem: {len(nome)} caracteres\n"
      f"Cidade tem: {len(cidade)} caracteres\n"
      f"CPF tem: {len(cpf)} caracteres\n")
print()
#Remova os pontos (.) e o hífen (–) da variável cpf.
print(f"Removendo caracteres especiais do cpf: {cpf.replace('123.456.789-00', '12345678900')}")