import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionato = df_ocorrencias[['estelionato', 'mes_ano']]
    df_estelionato = df_estelionato.groupby(['mes_ano']).sum(['estelionato']).reset_index()

    print(df_estelionato.head(12))
    print('\nDados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()    

try:
    df_estelionato_mes_ano = df_estelionato.groupby(['mes_ano']).sum().reset_index()
    print(df_estelionato_mes_ano)
    array_estelionato_mes_ano = np.array(df_estelionato_mes_ano['estelionato'])
    
    print('\nCalculando informações sobre padrão de estelionatos...')
    media_estelionato = (np.mean(array_estelionato_mes_ano))
    mediana_estelionato = (np.median(array_estelionato_mes_ano))
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato) * 100
    print(f'A média de estelionatos registrados é de {media_estelionato}')
    print(f'A médiana de estelionatos registrados é de {mediana_estelionato}')
    print(f'Índice de verificação de tendência central: {distancia_media_mediana:.2f}%')
    print()
    print('Analisando os dados apresentados, com base nos cálculos estatísticos para verificação de tendência central, verifica-se assimetria considerável, com tendência a um padrão de instabilidade de número de ocorrências desse tipo de crime ao longo do tempo.')

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()        
