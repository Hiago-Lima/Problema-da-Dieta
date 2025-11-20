
import pulp
import pandas as pd

# 1. Lista de alimentos e nutrientes
data = {
    'Alimentos': ['Pão Integral', 'Queijo Cottage', 'Mamão', 'Nozes', 'Salada Crua',
                  'Feijão', 'Arroz Integral', 'Frango Grelhado', 'Maçã', 'Tapioca',
                  'Ovo', 'Atum Ralado', 'Iogurte'],
    'Energia (kcal)': [136, 85, 45, 100, 25, 132, 25, 165, 72, 68, 77, 17, 99],
    'Proteína (g)': [4.6, 17.2, 0.8, 2.3, 1.5, 8.8, 0.5, 31.0, 0.3, 0.0, 6.2, 3.0, 3.9],
    'Cálcio (g)': [0.06, 0.03, 0.02, 0.00, 0.02, 0.03, 0.00, 0.02, 0.01, 0.00, 0.03, 0.00, 0.14],
    'Sódio (g)': [0.276, 0.013, 0.0055, 0.000, 0.080, 0.001, 0.000, 0.074, 0.001,
                   0.037, 0.139, 0.069, 0.053],
    'Ferro (g)': [0.10, 0.01, 0.01, 0.00, 0.03, 0.12, 0.00, 0.06, 0.01, 0.02, 0.03, 0.00, 0.00],
    'Vitaminas (g)': [0.00, 0.01, 0.77, 0.00, 0.93, 0.00, 0.00, 0.00, 0.12, 0.00, 0.06, 0.00, 0.02],
    'Preço (por porção)': [0.93, 5.24, 1.29, 3.05, 0.50, 0.63, 0.09, 0.89, 1.95, 0.21, 0.99, 0.61, 1.69]
}

df = pd.DataFrame(data)

# 2. Criar problema de otimização
prob = pulp.LpProblem("Dieta_Maria", pulp.LpMinimize)

# 3. Variáveis
alimentos = df['Alimentos'].tolist()
x = pulp.LpVariable.dicts("qtd", alimentos, lowBound=0, cat='Continuous')

# 4. Função objetivo
preco = dict(zip(df['Alimentos'], df['Preço (por porção)']))
prob += pulp.lpSum([preco[f] * x[f] for f in alimentos]), "Custo_Total"

# 5. Restrições de nutrientes (mínimos)
minimos = {'Energia (kcal)': 1870,
           'Proteína (g)': 46,
           'Vitaminas (g)': 0.775}

for nutriente in minimos:
    valores = dict(zip(df['Alimentos'], df[nutriente]))
    prob += pulp.lpSum([valores[f] * x[f] for f in alimentos]) >= minimos[nutriente]

# Máximos
prob += pulp.lpSum(dict(zip(df['Alimentos'], df['Sódio (g)']))[f] * x[f] for f in alimentos) <= 1.5
prob += pulp.lpSum(dict(zip(df['Alimentos'], df['Ferro (g)']))[f] * x[f] for f in alimentos) <= 0.018
prob += pulp.lpSum(dict(zip(df['Alimentos'], df['Cálcio (g)']))[f] * x[f] for f in alimentos) <= 1

# 6. Restrições de grupos
# Frutas
prob += x['Mamão'] + x['Maçã'] <= 1
# Leite e derivados
prob += x['Queijo Cottage'] + x['Iogurte'] <= 1

# Proteínas (carne, ovo, atum)
prob += x['Frango Grelhado'] + x['Ovo'] + x['Atum Ralado'] <= 1

# Cereais
prob += x['Pão Integral'] <= 1
prob += x['Arroz Integral'] <= 1

# Leguminosas / sementes / raízes
prob += x['Feijão'] <= 1
prob += x['Tapioca'] <= 1

# Vegetais livres
prob += x['Salada Crua'] >= 0


prob.solve()

# 7. Resultado
print("Status:", pulp.LpStatus[prob.status])
for f in alimentos:
    print(f"{f}: {x[f].varValue:.4f} porções")
print("\nCusto total: R$", round(pulp.value(prob.objective), 2))
