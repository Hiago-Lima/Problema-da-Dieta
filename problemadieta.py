# ===========================================================
# Problema da Dieta - Exemplo de Maria (com Pandas)
# Autor: (seu nome)
# ===========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
# -----------------------------------------------------------
# 1. Criar DataFrame com dados dos alimentos e nutrientes

dados = {
    'Alimento': [
        'Pão', 'Queijo', 'Mamão', 'Nozes', 'Salada crua', 'Feijão', 'Arroz',
        'Frango', 'Maçã', 'Tapioca', 'Ovo', 'Atum', 'Iogurte'
    ],
    'Custo_R$': [0.93, 5.24, 1.29, 3.05, 0.50, 0.63, 0.09, 0.89, 1.95, 0.21, 0.99, 0.61, 1.69],
    'Energia_kcal': [136, 85, 45, 100, 25, 132, 25, 165, 72, 68, 77, 17, 99],
    'Proteina_g': [4.6, 17.2, 0.8, 2.3, 1.5, 8.8, 0.5, 31.0, 0.3, 0.0, 6.2, 3.0, 3.9],
    'Calcio_g': [0.06, 0.03, 0.02, 0.0, 0.02, 0.03, 0.00, 0.02, 0.01, 0.0, 0.03, 0.0, 0.14],
    'Sodio_g': [0.276, 0.013, 0.0055, 0.0, 0.08, 0.001, 0.0, 0.074, 0.001, 0.037, 0.139, 0.069, 0.053],
    'Ferro_g': [0.10, 0.01, 0.01, 0.0, 0.03, 0.12, 0.0, 0.06, 0.01, 0.02, 0.03, 0.0, 0.0],
    'Vitaminas_g': [0.00, 0.01, 0.77, 0.0, 0.93, 0.00, 0.0, 0.00, 0.12, 0.0, 0.06, 0.0, 0.02]
}

df = pd.DataFrame(dados)
print("=== Dados dos Alimentos ===")
print(df, "\n")

# -----------------------------------------------------------
# 2. Vetores e matrizes do modelo
c = df['Custo_R$'].values

A = df[['Energia_kcal', 'Proteina_g', 'Calcio_g', 'Sodio_g', 'Ferro_g', 'Vitaminas_g']].T.values

b = np.array([1870, 46, 1.0, 1.5, 0.018, 0.775])

# Como o linprog resolve A_ub x <= b_ub, e aqui temos A x >= b,
# multiplicamos por -1 para inverter o sentido.
A_ub = -A
b_ub = -b

# Limites das variáveis (x >= 0)
bounds = [(0, None)] * len(df)

# -----------------------------------------------------------
# 3. Resolver o modelo
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# -----------------------------------------------------------
# 4. Mostrar resultados
if res.success:
    df['Porcao_ideal'] = res.x
    df['Custo_total_R$'] = df['Custo_R$'] * df['Porcao_ideal']

    print("=== SOLUÇÃO ENCONTRADA ===")
    print(df[['Alimento', 'Porcao_ideal', 'Custo_total_R$']])
    print("\nCusto mínimo total = R$ {:.2f}".format(res.fun))

    # Nutrientes atingidos (A x)
    nutrientes_totais = A.dot(res.x)
    df_nut = pd.DataFrame({
        'Nutriente': ['Energia_kcal', 'Proteina_g', 'Calcio_g', 'Sodio_g', 'Ferro_g', 'Vitaminas_g'],
        'Total_obtido': nutrientes_totais,
        'Necessario_minimo': b
    })
    print("\n=== Nutrientes atingidos ===")
    print(df_nut)
else:
    print("Solver não convergiu:", res.message)
