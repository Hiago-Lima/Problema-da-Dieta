#Nesse problema, pretende-se investigar a quantidade de cada alimento que Maria vai consumir e quanto de calorias vai ingerir.
import pandas as pd # mexer com base de dados(nesse caso, tabela)
import numpy as np # fazer cálculos numéricos
from scipy.optimize import linprog as simplex # minimizar ou maximizar funções

df = pd.read_excel("tabela_dieta.xlsx") # colocando a tabela em uma variável pra facilitar nossa vida
print("=== Dados dos Alimentos ===")
print(df, "\n")
# vetor de custos // é atribuído a c os valores da parte do dataframe(tabela) Preço
c = df['Energia (kcal)'].values
# matriz A , nutrientes dos alimentos //  atribui os valores de uma matriz transposta
A = df[['Proteína (g)', 'Cálcio (g)', 'Sódio (g)', 'Ferro (g)', 'Vitaminas (g)']].T.values
# vetor b (necessidades mínimas de Maria) // cria um vetor de utilizando o np
b = np.array([ 46, 1.0, 1.5, 0.018, 0.775])

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
    df['Porcao_ideal (g)'] = res.x
    # Multiplica cada porção pelo preço correspondente
    df['Calorias'] = df['Energia (kcal)'] * df['Porcao_ideal (g)']

    print("=== SOLUÇÃO ENCONTRADA ===")
    print(df[['Alimentos', 'Porcao_ideal (g)', 'Calorias']])
    #res.fun é o valor mínimo encontrado da função de custo.
    #{:.2f} formata com 2 casas decimais.
    print("\nCalorias mínimas totais {:.2f}".format(res.fun))

    # Nutrientes atingidos (A x)
    # Multiplica a matriz de nutrientes pela quantidade de porções escolhidas.
    nutrientes_totais = A.dot(res.x)
    #Criando uma tabela comparando atingido vs necessário:
    df_nut = pd.DataFrame({
        'Nutriente': ['Proteína (g)', 'Cálcio (g)', 'Sódio (g)', 'Ferro (g)', 'Vitaminas (g)'],
        'Total_obtido': nutrientes_totais,
        'Necessario': b
    })
    print("\n=== Nutrientes atingidos ===")
    print(df_nut)
    print("Essa solução é suficiente?")
    print("Ainda não pois")
else:
    print("Solver não convergiu:", res.message)
