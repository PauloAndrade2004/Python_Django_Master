# Função para simular o envio de email
def enviar_email(clientes):
    print(f'Email enviado para o cliente {clientes}')

clientes = ['Ana', 'Paulo', 'Gabrielle', 'Claudia', 'Diomeneis', 'Arthur']

# 1. Iterando diretamente sobre uma lista
print("1. Iterando diretamente sobre a lista:")
for cliente in clientes:
    enviar_email(cliente)

# 2. Usando enumerate() para obter o índice e o valor
print("\n2. Usando enumerate() com (break) para obter índice e valor:")
for i, cliente in enumerate(clientes):
    # Passou pelo índice 0. Passou pelo índice 1, apos isso quando chegou o índice 2, o programa para de enviar os email para o restante das pessoas.
    if i == 2:
        break
    enviar_email(cliente)

# 4. Usando o continue 
print("\n3. Usando continue:")
# continue , quando chega no índice 3, ele pula o indice 3 e envia o email para as outras pessoas.
for a, pessoa in enumerate(clientes):
    if a == 3:
        continue
    enviar_email(pessoa)

# 5. Usando range() para iterar sobre índices
print("\n4. Usando range() para iterar sobre índices:")
for i in range(len(clientes)):
    print(i, clientes[i])





