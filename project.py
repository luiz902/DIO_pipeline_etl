import pandas as pd

# Carregando o arquivo CSV em um DataFrame
file_path = "C:/Users/Luiz Neto/Downloads/vgsales.csv"
df = pd.read_csv(file_path)

# Visualizando as primeiras linhas do DataFrame para verificar os dados
print(df.head())

# Calculando o total de vendas por gênero
total_sales_by_genre = df.groupby('Genre')['Global_Sales'].sum()

# Calculando o total de vendas por ano
total_sales_by_year = df.groupby('Year')['Global_Sales'].sum()

# Visualizando os resultados das transformações
print("Total de Vendas por Gênero:")
print(total_sales_by_genre)

print("\nTotal de Vendas por Ano:")
print(total_sales_by_year)

# Salvando os dados transformados em um arquivo CSV
total_sales_by_genre.to_csv("total_vendas_por_genero.csv")
total_sales_by_year.to_csv("total_vendas_por_ano.csv")

# Alternativamente, criar uma visualização simples usando Matplotlib
import matplotlib.pyplot as plt

# Criando gráfico de barras para total de vendas por gênero
total_sales_by_genre.plot(kind='bar')
plt.xlabel('Gênero')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Gênero')
plt.show()

# Criando gráfico de linha para total de vendas por ano
total_sales_by_year.plot(kind='line', marker='o')
plt.xlabel('Ano')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Ano')
plt.show()