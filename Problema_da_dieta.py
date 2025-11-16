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

# aqui transformamos
A_ub = -A
b_ub = -b

# Limites das variáveis (x >= 0) * 13( quantidade de alimentos) minímas
bounds = [(0, None)] * len(df)
# Resolver o modelo utilizando o simplex()
# passa todos os parametros para resolver e utiliza o método highs
res = simplex(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Mostrar resultados
if res.success:
    # contém o valor de cada variável x
    df['Porcao_ideal'] = res.x
    # Multiplica cada porção pelo preço correspondente
    df['Custo_total_R$'] = df['Preço (por porção)'] * df['Porcao_ideal']

    print("=== SOLUÇÃO ENCONTRADA ===")
    print(df[['Alimentos', 'Porcao_ideal', 'Custo_total_R$']])
    #res.fun é o valor mínimo encontrado da função de custo.
    #{:.2f} formata com 2 casas decimais.
    print("\nCusto mínimo total = R$ {:.2f}".format(res.fun))

    # Nutrientes atingidos (A x)
    # Multiplica a matriz de nutrientes pela quantidade de porções escolhidas.
    nutrientes_totais = A.dot(res.x)
    #Criando uma tabela comparando atingido vs necessário:
    df_nut = pd.DataFrame({
        'Nutriente': ['Energia (kcal)', 'Proteína (g)', 'Cálcio (g)', 'Sódio (g)', 'Ferro (g)', 'Vitaminas (g)'],
        'Total_obtido': nutrientes_totais,
        'Necessario_minimo': b
    })
    print("\n=== Nutrientes atingidos ===")
    print(df_nut)
    print("Essa solução é suficiente?")
    print("Ainda não")
else:
    print("Solver não convergiu:", res.message)
