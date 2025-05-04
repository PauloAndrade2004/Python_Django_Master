
meu_dicionario = {
    # Chaves         Valores
    'Nome':         'Paulo',
    'Idade':        20,
    'Profissão':    'Dev',

    # Valor é uma lista
    'Interesses': ['Python', 'Java'],
    
    # Este dicionário armazena pares de chave e valor.
    # As chaves são strings, e os valores podem ser de qualquer tipo — até mesmo listas ou outros dicionários.

    # Um dicionário pode conter outro dicionário como valor de uma chave.
    'Endereco': {
        'Rua': 'Rua Sanhaçu',
        'Número': 310,
        'Cidade': 'São Paulo'
    }
}

# buscando o nome da pessoa que está dentro do nosso dicionario. Devemos passar o nome da chave que temos.
print(meu_dicionario.get('Nome'))

# buscando os interesses da nossa pessoa. Ele ira exibir a lista que esta dentro da nossa chave.
print(meu_dicionario.get('Interesses'))

# agora podemos buscar um Interesse expecifico da nossa pessoa. Adicionando o [] ==> Índice do nosso Interesse.
print(meu_dicionario.get('Interesses')[0])
