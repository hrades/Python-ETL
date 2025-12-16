import pandas as pd
import sqlite3
# Extract
url = 'https://raw.githubusercontent.com/Muralimekala/python/master/Salaries.csv'
sf = pd.read_csv(url)
print(sf.info())

# Transform
sf = sf.drop(columns=['Notes', 'Status'], errors='ignore') # Tirar colunas com dados insignificantes
# Arrumar colunas de dinheiro (transforma texto em número e vazios em 0)
colunas_dinheiro = ['BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits']
for col in colunas_dinheiro:
    sf[col] = pd.to_numeric(sf[col], errors='coerce')  # 'coerce' transforma erros (textos estranhos) em NaN
    sf[col] = sf[col].fillna(0.0) # Preenche os NaNs com 0.0
# Arruma os textos de caixa alta para 1a letra de cada palavra maiúscula
sf['EmployeeName'] = sf['EmployeeName'].str.title()
sf['JobTitle'] = sf['JobTitle'].str.title()

# Load
sf.to_csv('salarios_tratados.csv', index=False) # Salva em CSV
print("Arquivo 'salarios_tratados.csv' salvo com sucesso!")
# Salva em Banco SQLite
conexao = sqlite3.connect('banco_dados.db')
sf.to_sql('salarios', conexao, if_exists='replace', index=False)
conexao.close()
print("Dados salvos no banco SQLite 'banco_dados.db'!")
# Mostra o resultado final na tela
print("\n--- Primeiras 5 linhas ---")
print(sf.head(10))
