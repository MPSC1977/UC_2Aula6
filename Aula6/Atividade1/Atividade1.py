import os

os.system('cls')


from sqlalchemy import create_engine
import pandas as pd
import numpy as np

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_loja'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

df_estoque = pd.read_sql('tb_produtos', engine)
# print(df_estoque.head())

produto = df_estoque['NomeProduto']
preco_produto = df_estoque['Valor']

df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
df_agrupado = df_estoque.groupby('NomeProduto').agg({'QuantidadeEstoque': 'sum', 'TotalEstoque': 'sum'}).reset_index()
df_ordenado = df_agrupado.sort_values(by='TotalEstoque', ascending=False)

array_preco_produto = np.array(df_estoque['TotalEstoque'])
print(array_preco_produto)

media = np.mean(array_preco_produto)
mediana = np.median(array_preco_produto)
distancia = abs((media - mediana) / mediana) * 100
print(distancia)

print(f'A média dos preços dos produtos é: {media}')
print(f'A mediana dos preços dos produtos é: {mediana}')
print(f'A distância entre a média e mediana é de {distancia}')

print(df_agrupado)
print(df_ordenado[['NomeProduto', 'TotalEstoque']])



q1 = np.quantile(preco_produto, 0.25)
q2 = np.quantile(preco_produto, 0.50)
q3 = np.quantile(preco_produto, 0.75)

# print(f'O preço médio dos produtos em estoque é R${estoque_medio}')
# print(f'25% dos produtos em estoque tem preço inferior a R${q1}')
# print(f'25% dos produtos em estoque tem preço superior a R${q3}')
# print(df_estoque[['NomeProduto', 'TotalEstoque']])

# print(f'Total geral em estoque: R${df_estoque["TotalEstoque"].sum()}')