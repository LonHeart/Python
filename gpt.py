from operator import itemgetter

lista = []

for i in range(2):
    x = input("dia: ")
    y = input().split(" ")

    data = {
        'dia': int(x),
        'mês': int(y[0]),
        'ano': int(y[1]),
    }
    lista.append(data)

# Função para converter o dicionário em uma tupla (ano, mês, dia)
def converter_data(dicionario):
    return dicionario['ano'], dicionario['mês'], dicionario['dia']

# Encontrar a data mais antiga usando a função min() com itemgetter
data_mais_antiga = max(lista, key=converter_data)

print("A data mais recente é:", data_mais_antiga['dia'], data_mais_antiga['mês'], data_mais_antiga['ano'])
