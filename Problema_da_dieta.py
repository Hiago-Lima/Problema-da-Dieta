# acho q vou disponibilizar um arquivo excalidraw aq pra facilitar a compreensão do problema
import pandas as pd # mexer com base de dados(nesse caso, tabela)
import numpy as np # fazer cálculos numéricos
import matplotlib.pyplot as plt #plotar gráficos, nao sei se a gnt vai usar
from scipy.optimize import linprog # minimizar ou maximizar funções

df = pd.read_excel("tabela_dieta.xlsx") # colocando a tabela em uma variável pra facilitar nossa vida