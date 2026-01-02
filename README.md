# 🗳️ Análise de Dados Eleitorais - Duque de Caxias (RJ)

Este projeto realiza uma análise exploratória de dados históricos do TSE (Tribunal Superior Eleitoral), focando na evolução do comportamento do eleitor no município de Duque de Caxias/RJ.

## 🎯 Objetivos
- Analisar o histórico de votação para o cargo de Prefeito.
- Identificar tendências de **Abstenção** e votos **Brancos/Nulos** (Alienação Eleitoral).
- Validar a integridade dos dados comparando com fontes oficiais da imprensa (G1).

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Pandas** (Manipulação e análise de dados)
- **Matplotlib** (Visualização de dados - *futura implementação*)

## 📊 Principais Descobertas
A análise dos dados (2000-2024) revelou um fenômeno de desengajamento eleitoral:
- Em **2020**, houve o pico de alienação, onde cerca de **43%** do eleitorado não escolheu um candidato (soma de abstenções, brancos e nulos).
- Os dados do arquivo CSV foram validados e possuem **100% de precisão** quando comparados aos resultados oficiais divulgados pela mídia.

## 🚀 Como executar
1. Clone o repositório.
2. Instale as dependências: `pip install pandas`
3. Adicione o arquivo `br_tse_eleicoes_detalhes_votacao_municipio.csv` na raiz do projeto.
4. Execute o script: `python analise_dados.py`

---
*Desenvolvido por [ Tiago Nascimento de motta]  como parte do portfólio de Ciência de Dados.*
