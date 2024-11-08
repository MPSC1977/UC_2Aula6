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

df_estoque = pd.read_excel('tb_produtos.xlsx', engine)
print(df_estoque.head())

df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']

print(df_estoque[['NomeProduto', 'TotalEstoque']])

print(f'Total geral em estoque: R${df_estoque["TotalEstoque"].sum()}')