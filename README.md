# Problema da Dieta

## O que é?

O problema da dieta, é um exemplo de **PPL, ou seja, de um Problema de Programação Linear,** o qual consiste em minimizar uma função linear(seja ela de custo, caloria, etc) sujeita a diversas restrições lineares e com variáveis não negativas.  
Neste trabalho utilizaremos o caso de Maria, baseado no PDF ao final do texto. Após receber recomendações nutricionais, ela precisa seguir restrições que garantam uma quantidade mínima de nutrientes, ao mesmo tempo em que **deseja minimizar o custo total de sua dieta**. Em outras abordagens, também analisaremos a ingestão calórica e uma dieta com baixa ingestão de sódio

### Abordagens

Dada a tabela de valor nutricional e preço iremos discutir as seguintes situações:
| Alimentos | Energia (kcal) | Proteína (g) | Cálcio (g) | Sódio (g) | Ferro (g) | Vitaminas (g) | Tamanho da Porção (g) | Preço (por porção) |
|-----------------|----------------|--------------|------------|-----------|-----------|----------------|--------------------|---------------------|
| Pão Integral(x1) | 136 | 4.6 | 0.06 | 0.276 | 0.1 | 0 | 52 | 0.93 |
| Queijo Cottage(x2) | 85 | 17.2 | 0.03 | 0.013 | 0.01 | 0.01 | 100 | 5.24 |
| Mamão(x3)| 45 | 0.8 | 0.02 | 0.005 | 0.01 | 0.77 | 100 | 1.29 |
| Nozes(x4) | 100 | 2.3 | 0 | 0 | 0 | 0 | 15 | 3.05 |
| Salada Crua(x5) | 25 | 1.5 | 0.02 | 0.08 | 0.03 | 0.93 | 100 | 0.50 |
| Feijão(x6) | 132 | 8.8 | 0.03 | 0.001 | 0.12 | 0 | 100 | 0.63 |
| Arroz Integral(x7) | 25 | 0.5 | 0 | 0 | 0 | 0 | 20 | 0.09 |
| Frango Grelhado(x8) | 165 | 31 | 0.02 | 0.074 | 0.06 | 0 | 100 | 0.89 |
| Maçã(x9) | 72 | 0.3 | 0.01 | 0.001 | 0.01 | 0.12 | 140 | 1.95 |
| Tapioca(x10) | 68 | 0 | 0 | 0.037 | 0.02 | 0 | 20 | 0.21 |
| Ovo(x11)| 77 | 6.2 | 0.03 | 0.139 | 0.03 | 0.06 | 50 | 0.99 |
| Atum Ralado(x12) | 17 | 3 | 0 | 0.069 | 0 | 0 | 20 | 0.61 |
| Iogurte(x13) | 99 | 3.9 | 0.14 | 0.053 | 0 | 0.02 | 100 | 1.69 |

As abordagens serão:

1. Minimização do custo total, garantindo ingestão mínima de energia e de cada nutriente.

2. Investigação da quantidade de alimentos e ingestão calórica, considerando novamente o menor custo possível.

3. Dieta de baixa ingestão de sódio, analisando as quantidades consumidas e a ingestão final desse nutriente.

## Como isso será feito?

Inicialmente, vamos formalizar nosso PPL

**<div align="center">Minimizar Z = cTx</div>**

sujeitos ao conjunto de restrições:
**<div align="center">Ax≥b, x≥0</div>**

Onde:

- Z → valor da função objetivo (custo total)
- cᵀ → vetor de preços
- x → variáveis (quantidade de cada alimento)
- A → matriz com valores nutricionais
- b → exigências mínimas de nutrientes

Nosso objetivo é encontrar os valores de
𝑥
1
,
𝑥
2
,
…
,
𝑥
13
que satisfaçam todas as restrições e minimizem 𝑍  
Para isso vamos, desde já, separar as restrições básicas que vão aparecer em todas as abordagens :  
Restrição Proteína: 4, 6𝑥1 + 17, 2𝑥2 + 0, 8𝑥3 + 2, 3𝑥4 + 1, 5𝑥5 + 8, 8𝑥6 + 0, 5𝑥7 + 31𝑥8 + 0, 3𝑥9 + 0𝑥10 + 6, 2𝑥11 + 3𝑥12 + 3, 9𝑥13 ≥ 46  
Restrição Cálcio: 0, 06𝑥1 + 0, 03𝑥2 + 0, 02𝑥3 + 0𝑥4 + 0, 02𝑥5 + 0, 03𝑥6 + 0𝑥7 + 0, 02𝑥8 + 0, 01𝑥9 + 0𝑥10 + 0, 03𝑥11 + 0𝑥12 + 0, 14𝑥13 ≥ 1  
Restrição Sódio: 0, 276𝑥1 +0, 013𝑥2 +0, 0055𝑥3 +0𝑥4 +0, 08𝑥5 +0, 001𝑥6 +0𝑥7 + 0, 074𝑥8 + 0, 001𝑥9 + 0, 037𝑥10 + 0, 139𝑥11 + 0, 069𝑥12 + 0, 053𝑥13 ≥ 1, 5;  
Restrição Ferro: 0, 1𝑥1+0, 01𝑥2+0, 01𝑥3+0𝑥4+0, 03𝑥5+0, 12𝑥6+0𝑥7+0, 06𝑥8+ 0, 01𝑥9 + 0, 02𝑥10 + 0, 03𝑥11 + 0𝑥12 + 0𝑥13 ≥ 0, 018;  
Restrição Vitaminas: 0𝑥1 + 0, 01𝑥2 + 0, 77𝑥3 + 0𝑥4 + 0, 93𝑥5 + 0𝑥6 + 0𝑥7 + 0𝑥8 + 0, 12𝑥9 + 0𝑥10 + 0, 06𝑥11 + 0𝑥12 + 0, 02𝑥13 ≥ 0, 775;  
Restrição de Não-negatividade: 𝑥1, 𝑥2, 𝑥3, 𝑥4, 𝑥5, 𝑥6, 𝑥7, 𝑥8, 𝑥9, 𝑥10, 𝑥11, 𝑥12, 𝑥13 ≥ 0

Essas restrições podem ser ajustadas dependendo da abordagem (ex.: limites máximos, requisitos mais rígidos etc.).

### SIMPLEX

Dado que o número de variáveis é grande (13 alimentos), e todas as funções envolvidas são lineares.
Isso permite resolver o problema usando o método Simplex por meio da biblioteca scipy.

A região definida pelas restrições é um poliedro convexo, e uma propriedade chave da Programação Linear é:

    A solução ótima sempre ocorre em um vértice desse poliedro.

O Simplex navega entre esses vértices até encontrar aquele que fornece o menor custo possível para a dieta de Maria.

A PL também permite analisar o problema dual, que associa um valor a cada restrição nutricional.

No caso da dieta, o dual indica:

    Quanto o custo mínimo aumentaria se Maria precisasse de mais uma unidade de proteína, cálcio, ferro, sódio ou vitaminas.
    (no caso se a função objetivo for achar o custo mínimo)

Esses valores são chamados de preços sombra.
Eles revelam quais nutrientes são mais restritivos e quais mais influenciam o custo da dieta.
Agora, com tudo formalizado, vamos partir para a resolução de problema e suas abordagens.

## 1. Abordagem

Nesta abordagem, Maria quer montar uma dieta de menor custo possível, desde que atenda às quantidades mínimas de nutrientes recomendadas. O objetivo é descobrir quanto ela vai gastar e quantas porções de cada alimento são necessárias para atender esses requisitos.

A função objetivo usada para minimizar o custo é:
Min Custo =
0,93𝑥₁ + 5,24𝑥₂ + 1,29𝑥₃ + 3,05𝑥₄ + 0,50𝑥₅ + 0,63𝑥₆ + 0,09𝑥₇ + 0,89𝑥₈+1,95𝑥₉ + 0,21𝑥₁₀ + 0,99𝑥₁₁ + 0,61𝑥₁₂ + 1,69𝑥₁₃
E, entre as restrições, temos a exigência de energia mínima:
Calorias mínimas:
136𝑥₁ + 85𝑥₂ + 45𝑥₃ + 100𝑥₄ + 25𝑥₅ + 132𝑥₆ + 25𝑥₇ + 165𝑥₈+72𝑥₉ + 68𝑥₁₀ + 77𝑥₁₁ + 17𝑥₁₂ + 99𝑥₁₃ ≥ 1870

Além disso, as demais restrições mínimas iniciais. como proteína, vitaminas, cálcio, ferro e sódio também são incluídas no modelo.
Com a ajuda das bibliotecas pandas e PuLP, os dados da tabela são carregados, as variáveis são criadas e o problema de otimização é resolvido pelo método Simplex, buscando sempre o menor custo que ainda satisfaça todos os limites impostos.

### 1.1 Primeiro resultado

Compilando e executando o código com as restrições percebemos que o resultado é:

| Alimentos       | Porção Ideal | Quantidade Total (g) |
| --------------- | ------------ | -------------------- |
| Pão Integral    | 12.33        | 641.16               |
| Queijo Cottage  | 0.000000     | 0.000000             |
| Mamão           | 0.000000     | 0.000000             |
| Nozes           | 0.000000     | 0.000000             |
| Salada Crua     | 0.79         | 79                   |
| Feijão          | 0.000000     | 0.000000             |
| Arroz Integral  | 0.000000     | 0.000000             |
| Frango Grelhado | 0.000000     | 0.000000             |
| Maçã            | 0.000000     | 0.000000             |
| Tapioca         | 0.000000     | 0.000000             |
| Ovo             | 0.000000     | 0.000000             |
| Atum Ralado     | 0.0000       | 0.000000             |
| Iogurte         | 1.74         | 174                  |

O modelo recomendou 12,33 porções de pão integral, o que já estoura totalmente qualquer consumo humano aceitável para um único dia.
Apesar do custo ser baixo (R$ 14,81), essa solução não é nutricionalmente adequada, pois concentra praticamente toda a dieta em pão — ignorando o equilíbrio alimentar e levando a um excesso absurdo de carboidratos.

Por isso, fica claro que é necessário adicionar restrições de porções máximas por grupo alimentar antes de buscar uma solução saudável e realista.


### 1.2 Segundo resultado

Para que Maria consiga uma dieta com menor custo possível e uma quantidade mínima de nutrientes, deve-se restringir as variáveis à quantidade máxima de porções diária e utilizar as restrições dos nutrientes cálcio, sódio e ferro como menor igual.

### **As novas restrições adicionadas:**
**Frutas: No máximo 1 porção**
⇒ x3 + x9 <= 1
**Leite e Derivados: No máximo 1 porção**
⇒x2 + x13 <=1
**Proteínas (Carne, PVT, Ovo): No máximo 1 porção**
⇒ x8 + x11 + x13 <=1
**Cereais: No máximo 1 porção**
⇒ x1 <=1
⇒ x7 <=1
**Leguminosas; Sementes e Oleaginosas; Raízes e Tubérculos: No máximo 1 porção**
⇒ x6 <=1 
⇒ x10 <=1
**Vegetais: Livre**
⇒ x5>=0

A partir dessas novas restrições, chegamos no resultado:

| Alimento | Porção Ideal | Quantidade Total (g) |
|------------------|--------------|------------------------|
| Pão Integral     | 0.000000     | 0.000000 |
| Queijo Cottage   | 0.0000       | 0.000000 |
| Mamão            | 0.9805       | 98       |
| Nozes            | 16.58        | 248.7    |
| Salada Crua      | 0.00000      | 0.000000 |
| Feijão           | 0.000000     | 0.000000 |
| Arroz Integral   | 1.00         | 20       |
| Frango Grelhado  | 0.00000      | 0.00000  |
| Maçã             | 0.000000     | 0.000000 |
| Tapioca          | 0.40         | 8        |
| Ovo              | 0.000000     | 0.000000 |
| Atum Ralado      | 0.88         | 17.6     |
| Iogurte          | 1.00         | 100      |

com um custo de R$54, 26.
Assim, ao adicionar novas restrições, Maria obteve uma dieta mais equilibrada, com mais variedade de alimentos, com um custo diário minimizado e respeitando as quantidades mínimas de nutrientes.



## 2. Abordagem

Nesta abordagem, pretende-se investigar a quantidade de cada alimento que Maria vai consumir e quanto de calorias vai ingerir.
Para isso, será preciso ter como função objetivo:

**<div align="center">Min kcal = 136𝑥1 + 85𝑥2 + 45𝑥3 + 100𝑥4 + 25𝑥5 + 132𝑥6 +
25𝑥7 + 165𝑥8 + 72𝑥9 + 68𝑥10 + 77𝑥11 + 17𝑥12 + 99𝑥13;</div>**  
por enquanto, as mesmas restrições da parte inicial serão aplicadas aqui.

Utilizando o a biblioteca pandas, numpy e scipy é possível pegar os dados da tabela, fazer a construção das variáveis e utilizar o método simplex através da função "lingprog", o qual vai receber todos os parametros.

### 2.1 Primeiro resultado

Rodando o código com apenas essas restrições percebemos que o resultado é:

| Alimentos       | Porção Ideal | Quantidade Total (g) |
| --------------- | ------------ | -------------------- |
| Pão Integral    | 0.000000     | 0.000000             |
| Queijo Cottage  | 0.000000     | 0.000000             |
| Mamão           | 0.000000     | 0.000000             |
| Nozes           | 0.000000     | 0.000000             |
| Salada Crua     | 13.876689    | 1378g                |
| Feijão          | 0.000000     | 0.000000             |
| Arroz Integral  | 0.000000     | 0.000000             |
| Frango Grelhado | 0.000000     | 0.000000             |
| Maçã            | 0.000000     | 0.000000             |
| Tapioca         | 0.000000     | 0.000000             |
| Ovo             | 0.000000     | 0.000000             |
| Atum Ralado     | 1.686374     | 36.668356            |
| Iogurte         | 5.160473     | 516.886824           |

**Calorias mínimas totais:** **886.47**  
Essa solução é aceitável?
Matematicamente é, no entanto, nutricionalmente não.  
Porque, Maria irá ingerir 5, 16
vezes mais a quantidade máxima de iogurte, fazendo com que ela consuma mais calorias
diárias ao invés de reduzir. Para equilibrar esta dieta, deve-se inserir novas restrições ao
problema.

### 2.2 Segundo resultado

Para obtermos um novo resultado precisamos adicionar mais restrições, neste caso, restrições sobre as quantidades **máximas de porções** e utilizar
as restrições dos **nutrientes cálcio e sódio como menor igual e ferro como maior igual**.

**As novas restrições adicionadas:**  
Frutas: No máximo 1 porção ⇒ 𝑥3 + 𝑥9 ≤ 1  
Leite e Derivados: No máximo 1 porção ⇒ 𝑥2 + 𝑥13 ≤ 1  
Proteínas (Carne, PVT, Ovo): No máximo 1 porção ⇒ 𝑥8 + 𝑥11 + 𝑥13 ≤ 1  
Cereais: No máximo 1 porção ⇒ 𝑥1, 𝑥7 ≤ 1  
Leguminosas; Sementes e Oleaginosas; Raízes e Tubérculos: No máximo 1 porção
⇒ 𝑥4, 𝑥6, 𝑥10 ≤ 1  
Vegetais: Livre ⇒ 𝑥5 ≥ 0

Com essas novas restrições e alterando algumas restrições básicas, obtemos o seguinte resultado:  
| Alimento | Porção Ideal | Quantidade Total (g) |
|------------------|--------------|------------------------|
| Pão Integral | 0.000000 | 0.000000 |
| Queijo Cottage | 1.000000 | 100.000000 |
| Mamão | 0.000000 | 0.000000 |
| Nozes | 0.000000 | 0.000000 |
| Salada Crua | 0.822581 | 82.258065 |
| Feijão | 0.000000 | 0.000000 |
| Arroz Integral | 0.000000 | 0.000000 |
| Frango Grelhado | 0.889230 | 88.922997 |
| Maçã | 0.000000 | 0.000000 |
| Tapioca | 0.000000 | 0.000000 |
| Ovo | 0.000000 | 0.000000 |
| Atum Ralado | 0.000000 | 0.000000 |
| Iogurte | 0.000000 | 0.000000 |

**Calorias mínimas totais = 252.29 kcal**  
O que isso representa?
Agora, Maria obterá um consumo calórico menor, com maior
consumo de proteínas e ferro e respeitando a quantidade mínima de nutrientes. Assim, atingimos nosso objetivo inicial de investigar a quantidade de cada alimento que Maria vai consumir e quanto de calorias vai ingerir de forma a respeitar todas as restrições impostas ao problema.

## 3. Problema 7: Dieta Renal (Baixo Sódio)
Nesta abordagem, Maria está com problemas renais e necessita de uma dieta com a menor ingestão de sódio possível. Pretende-se investigar a quantidade de cada alimento que ela deve consumir para atingir os nutrientes necessários minimizando o sódio.
Para isso, a função objetivo será:

<div align="center">Min Sódio = 0,276𝑥1 + 0,013𝑥2 + 0,0055𝑥3 + ... + 0,053𝑥13;</div>

As restrições iniciais de nutrientes (Energia, Proteína, Cálcio, Ferro e Vitaminas) são mantidas como "maior ou igual" (mínimos necessários) nesta primeira etapa.

3.1 Primeiro resultado (Problema 7.0)
Rodando o código (ou observando a Tabela 4.5 do PDF) com apenas as restrições nutricionais básicas e minimizando o sódio, obtemos o seguinte resultado:

| Alimentos       | Porção Ideal | Quantidade Total (g) |
| --------------- | ------------ | -------------------- |
| Pão Integral    | 0.000000     | 0g                   |
| Queijo Cottage  | 0.000000     | 0g                   |
| Mamão           | 1.000000     | 100g                 |
| Nozes           | 19.649915    | 1964g                |
| Salada Crua     | 0.000000     | 0g                   |
| Feijão          | 0.000000     | 0g                   |
| Arroz Integral  | 0.000000     | 0g                   |
| Frango Grelhado | 0.000000     | 0g                   |
| Maçã            | 0.000000     | 0g                   |
| Tapioca         | 0.000000     | 0g                   |
| Ovo             | 0.000000     | 0g                   |
| Atum Ralado     | 0.000000     | 0g                   |
| Iogurte         | 0.000000     | 0g                   |

Sódio mínimo total: 0.005 g (aproximadamente) 

Esta solução é aceitável? Matematicamente sim, pois o sódio é quase zero. No entanto, nutricionalmente não. Maria teria que ingerir quase 2 kg de nozes (19,64 porções). Embora o sódio seja baixo, o excesso de selênio (abundante nas nozes) pode causar reações adversas graves, como toxicidade, irritabilidade e fraqueza muscular. Além disso, a dieta carece de variedade.

3.2 Segundo resultado (Problema 7.1)

Para equilibrar essa dieta e evitar a toxicidade das nozes, novas restrições são inseridas no modelo. Além de limitar as porções, altera-se a lógica de alguns nutrientes para evitar excessos (Proteína e Cálcio tornam-se "Menor ou Igual", enquanto Ferro e Vitaminas e Energia mantêm-se ou ajustam-se para garantir mínimos).

Novas restrições adicionadas (Baseado no PDF e Código):
- Frutas: $x_3 + x_9 \le 1$ 7
- Leite e Derivados: $x_2 + x_{13} \le 1$ 8
- Proteínas (Carne, Ovos): $x_8 + x_{11} + x_{13} \le 1$ 9
- Cereais: $x_1 + x_7 \le 1$ 10
- Leguminosas/Raízes: $x_4, x_6, x_{10} \le 1$ 11

Observação: No PDF, as Nozes ($x_5$) ficaram com restrição livre ($x_5 \ge 0$)12, o que explica o resultado abaixo ainda conter muitas nozes. No seu código Python, você tentou adicionar uma restrição explícita para nozes (restricao_nozes), o que forçaria um resultado diferente, mas seguindo os dados resultantes do documento oficial:

| Alimento        | Porção Ideal | Quantidade Total (g) |
| --------------- | ------------ | -------------------- |
| Pão Integral    | 0.000000     | 0g                   |
| Queijo Cottage  | 0.000000     | 0g                   |
| Mamão           | 1.000000     | 100g                 |
| Nozes           | 18.162430    | 1816g                |
| Salada Crua     | 0.005376     | 0.5g                 |
| Feijão          | 0.065322     | 6.5g                 |
| Arroz Integral  | 0.000000     | 0g                   |
| Frango Grelhado | 0.000000     | 0g                   |
| Maçã            | 0.000000     | 0g                   |
| Tapioca         | 0.000000     | 0g                   |
| Ovo             | 0.000000     | 0g                   |
| Atum Ralado     | 0.000000     | 0g                   |
| Iogurte         | 0.000000     | 0g                   |

Sódio mínimo total = 0.0055 g 14141414

O que isso representa?

Ao adicionar as restrições de "máximo 1 porção" para a maioria dos grupos, houve uma ligeira diversificação (entrada de feijão e salada crua). No entanto, como as nozes têm baixíssimo sódio, alta caloria e alta proteína, e no modelo do PDF elas não foram limitadas a "1 porção" (apenas $x_5 \ge 0$), o algoritmo ainda as escolheu massivamente para bater a meta calórica sem estourar o sódio.O resultado mostra que, para uma dieta renal funcional, seria necessário forçar matematicamente o limite de nozes (como você fez no seu código Python com restricao_nozes) para evitar a repetição do problema de toxicidade por selênio15.


### PDF

📄 [Clique aqui para abrir o PDF](./6_Problemadadieta.pdf)
