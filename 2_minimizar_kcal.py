#Nesse problema, pretende-se investigar a quantidade de cada alimento que Maria vai consumir e quanto de calorias vai ingerir.
import pandas as pd # mexer com base de dados(nesse caso, tabela)
import numpy as np # fazer cálculos numéricos
from scipy.optimize import linprog as simplex # minimizar ou maximizar funções

df = pd.read_excel("tabela_dieta.xlsx") # colocando a tabela em uma variável pra facilitar o uso
print("=== Dados dos Alimentos ===")
print(df, "\n")
# vetor de custos // é atribuído a c os valores da parte do dataframe(tabela) energia(kcal)
c = df['Energia (kcal)'].values
# matriz A , nutrientes dos alimentos //  atribui os valores de uma matriz transposta
A = df[['Proteína (g)', 'Cálcio (g)', 'Sódio (g)', 'Ferro (g)', 'Vitaminas (g)']].T.values
# vetor b (necessidades mínimas/máximas de Maria) // cria um vetor de restrições utilizando o np
b = np.array([ 46, 1.0, 1.5, 0.018, 0.775])

# aqui transformamos, pois o simplex do scipy trabalha com restrições do tipo <=
'''
caso só usássemos apenas as restrições do resultado 2.1
A_ub = -A
b_ub = -b
'''
A_ub = np.vstack([
    -A[0],   # proteína ≥ 46  → -proteína ≤ -46
     A[1],   # cálcio ≤ 1
     A[2],   # sódio ≤ 1.5
    -A[3],   # ferro ≥ 0.018 → -ferro ≤ -0.018
    -A[4],   # vitaminas ≥ 0.775 → -vitaminas ≤ -0.775
])

b_ub = np.array([ -46,1.0,1.5,-0.018,-0.775]) # vetor b modificado para as novas restrições
# Agora restrições para os grupos alimentares

# Frutas (x3 + x9 ≤ 1)
A_ub = np.vstack([A_ub, [0,0,1,0,0,0,0,0,1,0,0,0,0]])
b_ub = np.append(b_ub, 1)

# Leite e derivados (x2 + x13 ≤ 1)
A_ub = np.vstack([A_ub, [0,1,0,0,0,0,0,0,0,0,0,0,1]])
b_ub = np.append(b_ub, 1)

# Proteínas animais (x8 + x11 + x13 ≤ 1)
A_ub = np.vstack([A_ub, [0,0,0,0,0,0,0,1,0,0,1,0,1]])
b_ub = np.append(b_ub, 1)

# Cereais (x1 ≤ 1, x7 ≤ 1)
A_ub = np.vstack([A_ub, [1,0,0,0,0,0,0,0,0,0,0,0,0]])
b_ub = np.append(b_ub, 1)

A_ub = np.vstack([A_ub, [0,0,0,0,0,0,1,0,0,0,0,0,0]])
b_ub = np.append(b_ub, 1)

# Leguminosas/tubérculos/sementes (x4 ≤ 1, x6 ≤ 1, x10 ≤ 1)
A_ub = np.vstack([A_ub, [0,0,0,1,0,0,0,0,0,0,0,0,0]])
b_ub = np.append(b_ub, 1)

A_ub = np.vstack([A_ub, [0,0,0,0,0,1,0,0,0,0,0,0,0]])
b_ub = np.append(b_ub, 1)

A_ub = np.vstack([A_ub, [0,0,0,0,0,0,0,0,0,1,0,0,0]])
b_ub = np.append(b_ub, 1)

# Limites das variáveis (x >= 0) * 13( quantidade de alimentos) minímas
bounds = [(0, None)] * len(df)
# Resolver o modelo utilizando o simplex()
# passa todos os parametros para resolver e utiliza o método simplex do tipo highs
res = simplex(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Mostrar resultados
if res.success:
    # contém o valor de cada variável x
    df["Porção Ideal"] = res.x
    # Multiplica cada porção pelo tamanho da porção para obter a quantidade total em gramas.
    df["Quantidade Total (g)"] = df["Porção Ideal"] * df["Tamanho da Porção"]

    print("=== SOLUÇÃO ENCONTRADA ===")
    print(df[['Alimentos', 'Porção Ideal', 'Quantidade Total (g)']])
    # Calorias totais ingeridas
    total_calorias = np.sum(df["Energia (kcal)"] * df["Porção Ideal"])
    print("\nCalorias mínimas totais = {:.2f} kcal".format(total_calorias))

    # Nutrientes atingidos (A x)
    # Multiplica a matriz de nutrientes pela quantidade de porções escolhidas.
    nutrientes_totais = A.dot(res.x)
    #Criando uma tabela comparando atingido vs necessário:
    df_nut = pd.DataFrame({
        "Nutriente": ["Proteína", "Cálcio", "Sódio", "Ferro", "Vitaminas"],
        "Total Obtido": nutrientes_totais,
        "Valor Exigido": b # uns podem ser mínimos, outros máximos
    })
    print("\n=== Nutrientes obtidos ===")
    print(df_nut)
else:
    print("Solver não convergiu:", res.message)
