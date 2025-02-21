import pandas as pd

# Caminho do arquivo Excel
caminho_planilha = r"C:\Users\Julia\Downloads\Estudo\entrevistas.xlsx"

# Lendo a planilha
df = pd.read_excel(caminho_planilha)

# Corrigindo a coluna "entrevista com luiz"
df["entrevista com luiz"] = pd.to_datetime(df["entrevista com luiz"], errors="coerce")

# Salvando a versão corrigida
df.to_excel(r"C:\Users\Julia\Downloads\Estudo\entrevistas_corrigido.xlsx", index=False)

print("Arquivo corrigido salvo com sucesso!")