
meu_dicionario = {
    'Nome': 'Paulo',
    'Idade': 20,
    'Profissão': 'Dev'
}

# Usando o .get() para acessar um valor
print(meu_dicionario.get('Cidade'))

# Usando o .pop() para remover um valor
meu_dicionario.pop('Idade')  # Vai remover e retornar o valor 20

print(meu_dicionario.keys())  # Vai listar as chaves restantes: Nome, Cidade

# Usando o values() 
print(meu_dicionario.values())  # Vai listar os valores restantes: João, São Paulo