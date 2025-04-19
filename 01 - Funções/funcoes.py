
# Função com Parâmetros
def funcao_parametro(nome, idade):
    print(f"Meu nome é: {nome} e tenho {idade} anos!")
funcao_parametro("Paulo Cesar", 20) # Chamando a função 

    
def somar(a, b):
    resultado1 = a + b # podemos criar uma variável para armazenar o valor. É depois imprimir essa variável.
    print(f"A soma total dos números é: {resultado1}")
somar(32, 44)

# CRIANDO UMA FUNÇÃO COM RETORNO
def somar(c, d):
    resultado2 = c + d
    return resultado2 # nosso retorno pode ter ou nao ter alguma mensagem 
resultado2 = somar(2, 2)
print(resultado2) # SAIDA: 4

def multiplicar_numero(a, b, c):
    resultado3 = a * b * c 
    return f"A multiplicação dos números é: {resultado3}"
# Chamamos essa função sem precisar asmazenar a nossa função dentro de outra variável.
print(multiplicar_numero(3, 3, 4)) # SAIDA: 36 

# Exemplo criando funções personalizadas.
lista_clientes = []
def enviar_informacoes():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    lista_clientes.append({"nome": nome, "email": email})
    return "Cadastro realizado com sucesso!\n"

def visualizar_cadastro():
    print("\nClientes cadastrados:")
    for cliente in lista_clientes:
        print(f"Nome: {cliente['nome']} | Email: {cliente['email']}")

# Execução
enviar_informacoes()
visualizar_cadastro()

    