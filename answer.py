# 1) Valor da variável SOMA após o processamento do código:
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)  # O valor de SOMA será 91


# 2) Verificação se um número pertence à sequência de Fibonacci:
def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


# Exemplo de uso
numero_verificar = 21  # Você pode mudar o número aqui
print(verifica_fibonacci(numero_verificar))


# 3) Lógica e completar os próximos elementos:
# a) 1, 3, 5, 7, __9__
# b) 2, 4, 8, 16, 32, 64, __128__
# c) 0, 1, 4, 9, 16, 25, 36, __49__
# d) 4, 16, 36, 64, __100__
# e) 1, 1, 2, 3, 5, 8, __13__
# f) 2, 10, 12, 16, 17, 18, 19, __20__


# 4) Descobrir qual interruptor controla cada lâmpada:
# - Ligue um interruptor e espere alguns minutos
# - Desligue o interruptor e ligue outro
# - Entre na sala
# - A lâmpada acesa está conectada ao primeiro interruptor ligado
# - A lâmpada que está quente, mas não acesa, está conectada ao segundo interruptor ligado
# - A lâmpada que está fria está conectada ao interruptor que não foi ligado


# 5) Inverter os caracteres de uma string sem usar funções prontas:
def inverte_string(string):
    invertida = ''
    for char in string:
        invertida = char + invertida
    return invertida


# Exemplo de uso
string_original = "hello"  # Você pode mudar a string aqui
print("String original:", string_original)
print("String invertida:", inverte_string(string_original))
