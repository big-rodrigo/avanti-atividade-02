# 1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares
def impares_de_pares(lista_pares):
    return [par + 1 for par in lista_pares]


# 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
def filtrar_primos(lista_num):
    def is_primo(numero):
        if numero <= 1:
            return False
        if numero == 2:
            return True
        if numero % 2 == 0:
            return False
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                return False
        return True

    return [num for num in lista_num if is_primo(num)]


# 3. Escreva uma função que receba duas listas e retorne outra lista com os
# elementos que estão presentes em apenas uma das listas.
def merge_listas(lista1, lista2):
    set1 = set(lista1)
    set1.update(set(lista2))
    return list(set1)


#4. Dada uma lista de números inteiros, escreva uma função para encontrar o
#segundo maior valor na lista.
def segundo_maior(lista):
    segundo_maior = 0
    maior = 1
    for i, num in enumerate(lista):
        if num > lista[maior]:
            segundo_maior = maior
            maior = i
    
    return lista[segundo_maior]


# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o
# nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das
# pessoas em ordem alfabética.
def ordenar_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda pessoa: pessoa[0])
    

# 6. Observe os espaços sublinhados e complete o código.
# import matplotlib.pyplot as plt
# import numpy as np
# fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")
# for row in range(2):
    # for col in range(2):
        # axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5), transform=axs[row, col].transAxes, ha='center', va='center', fontsize=18, color='darkgrey')
# fig.suptitle('plt.subplots()')


# 7. Observe os espaços sublinhados e complete o código.
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)


# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um
# DataFrame e exibir as primeiras linhas?
import pandas as pd
dataframe = pd.read_csv("arquivo.csv")
print(dataframe.head())


# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas
# em um “DataFrame” com base em uma condição?
import pandas as pd
coluna_idade = df['idade']
linhas_filtradas = df[df['idade'] > 30]


# 10.Utilizando pandas, como lidar com valores ausentes (NaN) em um
# DataFrame?
# Para lidar com valores ausentes (NaN) em um DataFrame pandas, é possível usar métodos como isna(), fillna() e dropna().