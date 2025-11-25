import pandas as pd
import numpy as np  
from scipy.optimize import linprog

data = {
    'Alimentos': ['Pão Integral', 'Queijo Cottage', 'Mamão', 'Nozes', 'Salada Crua',
                  'Feijão', 'Arroz Integral', 'Frango Grelhado', 'Maçã', 'Tapioca',
                  'Ovo', 'Atum Ralado', 'Iogurte'],
    'Energia (kcal)': [136, 85, 45, 100, 25, 132, 25, 165, 72, 68, 77, 17, 99],
    'Proteína (g)': [4.6, 17.2, 0.8, 2.3, 1.5, 8.8, 0.5, 31.0, 0.3, 0.0, 6.2, 3.0, 3.9],
    'Cálcio (g)': [0.06, 0.03, 0.02, 0.00, 0.02, 0.03, 0.00, 0.02, 0.01, 0.00, 0.03, 0.00, 0.14],
    'Sódio (g)': [0.276, 0.013, 0.005, 0.000, 0.080, 0.001, 0.000, 0.074, 0.001, 0.037, 0.139, 0.069, 0.053],
    'Ferro (g)': [0.10, 0.01, 0.01, 0.00, 0.03, 0.12, 0.00, 0.06, 0.01, 0.02, 0.03, 0.00, 0.00],
    'Vitaminas (g)': [0.00, 0.01, 0.77, 0.00, 0.93, 0.00, 0.00, 0.00, 0.12, 0.00, 0.06, 0.00, 0.02],
    'Preço (por porção)': [0.93, 5.24, 1.29, 3.05, 0.50, 0.63, 0.09, 0.89, 1.95, 0.21, 0.99, 0.61, 1.69]
}

df = pd.DataFrame(data)
numero_linhas = len(df)
print(df)

# ==================================================
# PROBLEMA 7.0 DO PROBLEMA 
# ==================================================

funcao_objetivo_problema = df['Sódio (g)'].values

colunas_restricoes = ['Energia (kcal)', 'Proteína (g)', 'Cálcio (g)', 'Ferro (g)', 'Vitaminas (g)']
matriz_restricoes_nutrientes = df[colunas_restricoes].values.T

sinais_restricoes = np.array([-1, -1, -1, -1, -1])
matriz_restricoes_nutrientes_ii = matriz_restricoes_nutrientes * sinais_restricoes[:, np.newaxis]
vetor_limites_nutrientes = np.array([1870, 46, 1, 0.018, 0.775]) * sinais_restricoes

limites = [(0, None) for _ in range(numero_linhas)]

resultado_problema_7 = linprog(
    funcao_objetivo_problema, 
    A_ub = matriz_restricoes_nutrientes_ii,
    b_ub = vetor_limites_nutrientes,
    bounds = limites,
    method = 'highs'
)

# =====================================================
# RESULTADOS DO PROBLEMA 7
# =====================================================

print("Status: ", resultado_problema_7.message)
print("Sucesso: ", resultado_problema_7.success)
if resultado_problema_7.success:
    print ("Valor da quantidade de sodío minimizado: ", resultado_problema_7.fun, "g")

    #==========================================================
    # QUANTIDADE DE CADA PORÇAO
    #==========================================================
for i, alimento in enumerate(df['Alimentos']):
        quantidade = resultado_problema_7.x[i]# Mostra apenas alimentos com quantidade significativa
        print(f"{alimento:<20}: {quantidade:>8.4f} porções")


# ============================================================
# PROBLEMA 7.1 
# ============================================================
restricao_frutas = np.zeros(numero_linhas); restricao_frutas[[2, 8]] = 1
restricao_laticinios = np.zeros(numero_linhas); restricao_laticinios[[1, 12]] = 1
restricao_proteinas = np.zeros(numero_linhas); restricao_proteinas[[7, 11, 12]] = 1
restricao_cereais = np.zeros(numero_linhas); restricao_cereais[[0, 6]] = 1
restricao_nozes = np.zeros(numero_linhas); restricao_nozes[3] = 1
restricao_feijao = np.zeros(numero_linhas); restricao_feijao[5] = 1
restricao_tapioca = np.zeros(numero_linhas); restricao_tapioca[9] = 1

matriz_restricoes_porcoes = np.vstack([
    restricao_frutas, restricao_laticinios, restricao_proteinas,
    restricao_cereais, restricao_nozes, restricao_feijao, restricao_tapioca
])

sinal_porcao = -1  # -1 para "Pelo menos", 1 para "No máximo"
vetor_limites_porcoes = np.array([1, 1, 1, 1, 1, 1, 1]) * sinal_porcao
matriz_restricoes_porcoes = matriz_restricoes_porcoes * sinal_porcao
sinais_restricoes_7_1 = np.array([-1, 1, 1, -1, -1])
matriz_restricoes_ajustada_7_1 = matriz_restricoes_nutrientes * sinais_restricoes_7_1[:, np.newaxis]
vetor_limites_nutrientes_7_1 = np.array([1870, 46, 1, 0.018, 0.775]) * sinais_restricoes_7_1
matriz_restricoes_totais_7_1 = np.vstack([matriz_restricoes_ajustada_7_1, matriz_restricoes_porcoes])
vetor_limites_totais_7_1 = np.concatenate([vetor_limites_nutrientes_7_1, vetor_limites_porcoes])


# Resolver o Problema 7.1
resultado_problema_7_1 = linprog(
    funcao_objetivo_problema,
    A_ub=matriz_restricoes_totais_7_1,
    b_ub=vetor_limites_totais_7_1,
    bounds=limites,
    method='highs'
)

print("Status: ", resultado_problema_7_1.message)
print("Sucess: ", resultado_problema_7_1.success)

#===================================================================================
# RESULTADO DO PROBLEMA 7.1
# =================================================================================

if resultado_problema_7_1.success:
    print(f"Sódio Mínimo: {resultado_problema_7_1.fun:.4f} g")
    print("\nDieta Sugerida:")
for i, alimento in enumerate(df['Alimentos']):
    qtd = resultado_problema_7_1.x[i]
    print(f"{alimento:<20}: {qtd:>8.4f} porções")

