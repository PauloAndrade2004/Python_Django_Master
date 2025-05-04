
meu_dicionario = {
    # Chaves         Valores
    'Nome':         'Paulo',
    'Idade':        20,
    'Profissão':    'Dev',
    'pet': {
        'cachorro': 'Loki',
        'raca': 'Cani Corso',
        'idade cachorro': '8'
    },

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

# Exibindo o dicionario dentro da nossa (chave) 'pet'
print(meu_dicionario.get('pet'))
# Exibindo o dicionario 'pet' com o índice expecifico.
    # Em dicionario devo buscar atraves do (nome) da nossa (chave)
print(meu_dicionario.get('pet')['cachorro']) # Loki
    