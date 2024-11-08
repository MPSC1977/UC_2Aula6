import pandas as pd
import numpy as np

try:
    print('Obtendo dados...')

    ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estelionato = df_ocorrencias[['mes', 'estelionato']]
    df_estelionato = df_estelionato.groupby(['mes']).sum(['estelionato']).reset_index()

    print(df_estelionato.head(12))
    print('\nDados obtidos com sucesso!')

except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()    

try:
    print('\nCalculando informações sobre padrão de estelionatos...')
    array_estelionato = np.array(df_estelionato['estelionato'])
    media_estelionato = int(np.mean(array_estelionato))
    mediana_estelionato = int(np.median(array_estelionato))
    distancia_media_mediana = abs((media_estelionato - mediana_estelionato) / mediana_estelionato) * 100
    print(f'A média de estelionatos registrados é de {media_estelionato}')
    print(f'A médiana de estelionatos registrados é de {mediana_estelionato}')
    print(f'Índice de verificação de tendência central: {distancia_media_mediana:.2f}%')
    print()
    print('Analisando os dados apresentados e baseando-se em cálculos estatísticos, pode-se afirmar que há uma tendência simétrica de casos de estelionatos praticados durante os meses do ano, o que mostra um padrão estável de ocorrências desses crimes ao longo do tempo.')

except Exception as e:
    print(f'Erro ao obter informações sobre padrão de roubo de veículos: {e}')
    exit()        