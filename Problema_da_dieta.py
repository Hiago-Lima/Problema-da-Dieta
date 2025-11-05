# acho q vou disponibilizar um arquivo excalidraw aq pra facilitar a compreensão do problema
import pandas as pd # mexer com base de dados(nesse caso, tabela)
import numpy as np # fazer cálculos numéricos
import matplotlib.pyplot as plt #plotar gráficos, nao sei se a gnt vai usar
from scipy.optimize import linprog as simplex # minimizar ou maximizar funções

df = pd.read_excel("tabela_dieta.xlsx") # colocando a tabela em uma variável pra facilitar nossa vida
print("=== Dados dos Alimentos ===")
print(df, "\n")
# vetor de custos // é atribuído a c os valores da parte do dataframe(tabela) Preço
c = df['Preço (por porção)'].values
# matriz A , nutrientes dos alimentos //  atribui os valores de uma matriz transposta
A = df[['Energia (kcal)', 'Proteína (g)', 'Cálcio (g)', 'Sódio (g)', 'Ferro (g)', 'Vitaminas (g)']].T.values
# vetor b (necessidades mínimas de Maria) // cria um vetor de utilizando o np
b = np.array([1870, 46, 1.0, 1.5, 0.018, 0.775])