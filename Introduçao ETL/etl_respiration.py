import pandas as pd
# Extract
url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Resp2.csv'
df = pd.read_csv(url)

# Transform
# Padronizar de nomes de colunas
df.columns = df.columns.str.strip().str.lower()
# Agrupamento: Calcular a média e desvio padrão da respiração para cada nível de experiência
df_stats = df.groupby('experience')['respiration'].agg(['mean', 'std', 'count']).reset_index()
df_stats.columns = ['Nivel_Experiencia', 'Media_Respiracao', 'Desvio_Padrao', 'Contagem']
df_stats = df_stats.round(2) # 2 casas decimais

# Load
# Salvar os dados tratados
df.to_csv('dados_limpos.csv', index=False)
# Salvar os dados analíticos (novos - calculados)
df_stats.to_csv('relatorio_estatistico.csv', index=False)
# Mostrar resultado no terminal
print("--- Dados Agregados (Transformados) ---")
print(df_stats)
