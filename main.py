from modules.calculator import Calculator
from modules.utils import Utils

#https://www.kaggle.com/datasets/alroger/bolsa-familia/data
#low_income_families é o total de familias de baixa renda
#families é o total de familias de baixa renda que receberam apoio do bolsa família

#o dataset vai de 2011 a 2017, no entanto, como 2017 só vai até o mês 5, decidimos remover esse ano do dataset

statistics_calculator = Calculator()
data_utils = Utils()

content = data_utils.read_csv("csv/Bolsa_Familia_by_Region.csv")

#tem que arrumar a coluna de funding, ela vem com um sinal de $ junto d numero e virgula separando as casas decimais
content['funding'] = content['funding'].str.replace('$', '')
content['funding'] = content['funding'].str.replace(',', '').astype(float)

#---===---===---=== Cópia do dataset para melhor visualização ===---===---===---

content_by_million = content.copy()
content_by_million['funding'] = content_by_million['funding'] / 1000000
content_by_million['families'] = content_by_million['families'] / 1000000
content_by_million['low_income_families'] = content_by_million['low_income_families'] / 1000000

#---===---===---=== Definição das variáveis ===---===---===---

families_content = content['families']
funding_content = content['funding']
low_income_content = content['low_income_families']

statistics = {}

#---===---===---=== Cálculo da média ===---===---===---

statistics['media_familias_contempladas'] = statistics_calculator.calc_media(families_content)
statistics['media_investimento'] = statistics_calculator.calc_media(funding_content)
statistics['media_familias_baixa_renda'] = statistics_calculator.calc_media(low_income_content)

#---===---===---=== Mediana ===---===---===---

statistics['mediana_familias_contempladas'] = statistics_calculator.calc_mediana(families_content)
statistics['mediana_investimento'] = statistics_calculator.calc_mediana(funding_content)
statistics['mediana_familias_baixa_renda'] = statistics_calculator.calc_mediana(low_income_content)

#---===---===---=== Moda ===---===---===---

# statistics['moda_familias_contempladas'] = statistics_calculator.calc_moda(families_content)
# statistics['moda_investimento'] = statistics_calculator.calc_moda(funding_content)
statistics['moda_familias_baixa_renda'] = statistics_calculator.calc_moda(low_income_content)

#---===---===---=== Variança ===---===---===---

statistics['varianca_familias_contempladas'] = statistics_calculator.calc_varianca(families_content)
statistics['varianca_investimento'] = statistics_calculator.calc_varianca(funding_content)
statistics['varianca_familias_baixa_renda'] = statistics_calculator.calc_varianca(low_income_content)

#---===---===---=== Desvio padrão ===---===---===---

statistics['desvio_padrao_familias_contempladas'] = statistics_calculator.calc_desvio_padrao(families_content)
statistics['desvio_padrao_investimento'] = statistics_calculator.calc_desvio_padrao(funding_content)
statistics['desvio_padrao_familias_baixa_renda'] = statistics_calculator.calc_desvio_padrao(low_income_content)

for key, value in statistics.items():
    print(f"{key}: {value}")

#O dataset é separado em ano, mês e região. Junta os totais de cada ano

annual_totals = statistics_calculator.calcula_total_anual(content_by_million)

years = list(annual_totals.keys())

total_families = []
for year in years:
    total_families.append(annual_totals[year]['total_familias'])

total_low_income_families = []
for year in years:
    total_low_income_families.append(annual_totals[year]['total_familias_baixa_renda'])


#Plota um histograma da relação entre o ano e o total de familias abordadas pelo bolsa familia / total de familias baixa renda
data_utils.plot_histogram(years, total_families, "Ano", "Total de Famílias Abordadas (em Milhões) ", "Total de Famílias Abordadas por Ano")
data_utils.plot_histogram(years, total_low_income_families, "Ano", "Total de Famílias de Baixa Renda (em Milhões)", "Total de Famílias de Baixa Renda por Ano")


#Plota um boxplot da relação entre região e familias contempladas / investimento na região
data_utils.plot_boxplot(content_by_million, 'region', 'families', "Região", "Total de Famílias Atendidas (em Milhões)", "Distribuição do Total de Famílias Atendidas por Região")
data_utils.plot_boxplot(content_by_million, 'region', 'funding', "Região", "Total de Investimento (em Milhões)", "Distribuição do Total de Investimento por Região")


#Cria uma lista com os valores de investimento e de familias contempladas para usar no calculo de correlação e regressão linear
funding_values = list(content_by_million['funding'])
families_values = list(content_by_million['families'])


#Calcula pearson
pearson, correlation = statistics_calculator.calc_pearson(funding_values, families_values)
print(f"Coeficiente de Pearson: {pearson}, Correlação entre Investimento e Familias atendidas: {correlation}")


#plota um scatter entre o investimento e as familias contempladas
data_utils.plot_scatterplot(content_by_million, 'funding', 'families', "Investimento em Milhões", "Total de Famílias Atendidas (em Milhões)", "Relação entre Investimento e Total de Famílias Atendidas")


#Regressão linear
alpha, beta = statistics_calculator.calc_regression(funding_values, families_values)
predicted_values = statistics_calculator.predict_values(alpha, beta, funding_values)

r_squared = pearson ** 2

data_utils.plot_regression(content_by_million, 'funding', 'families', predicted_values, "Investimento (em Milhões)", "Total de Famílias Atendidas (em Milhões)", "Dispersão entre Investimento e Famílias Atendidas com Reta Ajustada da Regressão Linear")

print(f"Coeficiente Angular (Beta): {beta:.2f}")
print(f"Interseção (Alpha): {alpha:.2f}")
print(f"Coeficiente de Determinação (R²): {r_squared:.2f}") 
