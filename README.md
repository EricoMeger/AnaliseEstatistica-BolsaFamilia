# Análise Estatística do Bolsa Família

Este projeto realiza uma análise estatística do programa Bolsa Família, utilizando um dataset público disponível no Kaggle. A análise abrange desde estatísticas descritivas até regressão linear, além de visualizações de dados para melhor entendimento das variáveis. Uma das limitações do trabalho era fazer as funções manualmente, não podendo usar funções prontas como *mean()* ou *mode()*, por exemplo.

## Sumário

- [Referência do Dataset](#referência-do-dataset)
- [Requisitos](#requisitos)
- [Utilização do Docker](#utilização-do-docker)
- [Executando Localmente](#executando-localmente)
- [Análises Realizadas](#análises-realizadas)
- [Resultados e Interpretação](#resultados-e-interpretação)

## Referência do Dataset

Os dados utilizados neste projeto foram extraídos do Kaggle:

- Dataset: [Bolsa Família Dataset](https://www.kaggle.com/datasets/alroger/bolsa-familia/data) por Al Roger.

## Requisitos

Antes de executar o projeto, certifique-se de que você possui os seguintes pacotes instalados:

- **pandas** - Para manipulação e análise de dados
- **seaborn** - Para visualizações estatísticas
- **matplotlib** - Para criação de gráficos

Você pode instalar os pacotes diretamente usando `pip`:

```bash
$ pip install -r requirements.txt
```
## Executando o projeto

É possível executar o projeto de duas formas: via Docker ou localmente.

## Utilização do Docker

Para facilitar a execução do projeto, foi criado um container Docker com a configuração necessária para rodar a análise.

### Dockerfile

O Dockerfile utilizado para este projeto é configurado para rodar um ambiente Python com todas as dependências já instaladas. O problema é que o container não tem um ambiente gráfico, portanto, não é possível visualizar os gráficos por ele. No entanto, os gráficos são salvos na pasta _images_, tendo sido desenvolvido um script bash para mover automaticamente os gráficos salvos na pasta do docker para a pasta do projeto.

### Executando o Docker

Para executar o Docker, utilize o script bash desenvolvido:

### Dê permissão de execução para o script:

```bash
$ chmod +x get_docker_graphs.sh
```

### Execute o script:

```bash
$ ./get_docker_graphs.sh
```

## Rodando localmente

Para rodar localmente, certifique-se de ter as dependências mencionadas previamente já instaladas.

### Rodando o projeto

```bash
$ python main.py
```

## Análises Realizadas

Foram realizadas diversas análises estatísticas com base no dataset do Bolsa Família, abrangendo estatísticas descritivas, distribuição de dados, correlação entre variáveis e regressão linear. Abaixo estão as principais etapas e gráficos gerados:

### a) Estatísticas Descritivas

1. Média, Mediana, Moda, Desvio Padrão e Variância:
   - Foram calculadas a média, mediana, moda, desvio padrão e variância das variáveis contínuas, incluindo o investimento e o total de famílias atendidas pelo programa, fornecendo uma visão geral das tendências e dispersões dos dados.

### b) Distribuição dos Dados

  1. Histogramas:
     - Foi gerado um histograma do total de famílias de baixa renda por ano, mostrando a distribuição ao longo do tempo.
     - Outro histograma foi criado para o total de famílias abordadas pelo programa por ano, revelando variações no atendimento ao longo dos anos.

  2. Boxplots:
     - O boxplot do total de investimento por região foi gerado para identificar como os investimentos se distribuem entre as diferentes regiões do Brasil.
     - Também foi criado um boxplot do total de famílias atendidas por região, fornecendo uma visão sobre a distribuição dos atendimentos regionais.

### c) Correlação entre Variáveis

   1. Correlação de Pearson:
     - O coeficiente de correlação de Pearson foi 0.9709, o que indica uma correlação muito forte entre o investimento e o total de famílias atendidas. Isso sugere que, à medida que os investimentos aumentam, mais famílias são atendidas pelo programa.

   2. Gráfico de Dispersão (Scatter Plot):
     - Um gráfico de dispersão foi gerado para visualizar a relação entre o investimento e o total de famílias atendidas, permitindo identificar a tendência linear entre essas variáveis.

### d) Regressão Linear

   1. Modelo de Regressão Linear Simples:
      - Foi aplicada uma regressão linear simples para analisar a relação entre o investimento (variável independente) e o total de famílias atendidas (variável dependente).
      - Os resultados foram:
        - **Coeficiente angular (Beta):** 0.01
        - **Interseção (Alpha):** 0.23
        - **Coeficiente de Determinação (R²):** 0.94

  O R² indica que 94% da variação no número de famílias atendidas pode ser explicada pelo investimento. O gráfico de dispersão com a reta ajustada da regressão mostra a tendência positiva entre as duas variáveis.

## Resultados e Interpretação

  1. Histograma de Famílias de Baixa Renda por Ano (2011-2016):
     - Entre 2011 e 2016, a quantidade de famílias de baixa renda atendidas pelo programa Bolsa Família não apresentou mudanças bruscas, mantendo-se estável.

  2. Histograma de Famílias Abordadas pelo Programa por Ano (2011-2016):
     - Houve um crescimento no número de famílias atendidas de 2011 a 2014, com pico em 2014, e um declínio gradual entre 2015 e 2016.

  3. Correlação de Pearson:
     - A correlação de 0.9709 indica uma relação muito forte entre o investimento e o total de famílias atendidas.

  4. Regressão Linear:
     - O coeficiente de determinação R² = 0.94 sugere que a maior parte da variação no número de famílias atendidas é explicada pelo investimento.
