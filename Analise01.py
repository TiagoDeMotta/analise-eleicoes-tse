import pandas as pd

# Configurações de visualização
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.1f}%'.format

print("--- DUELO: PREFEITO vs VEREADOR EM CAXIAS ---\n")

arquivo = "br_tse_eleicoes_detalhes_votacao_municipio.csv"
df = pd.read_csv(arquivo)

# 1. Filtros: Caxias (3301702) e 1º Turno
filtro = (df['id_municipio'] == 3301702) & (df['turno'] == 1)
caxias = df[filtro].copy()

# 2. Engenharia de Dados: Criar métricas percentuais
# % de votos "jogados fora" (Brancos + Nulos) sobre o total que compareceu
caxias['% Perdidos'] = ((caxias['votos_brancos'] + caxias['votos_nulos']) / caxias['comparecimento']) * 100

# 3. Preparar a Tabela Comparativa
# Vamos usar o pivot_table para colocar Prefeito e Vereador lado a lado
tabela_comparativa = caxias.pivot_table(
    index='ano',
    columns='cargo',
    values='% Perdidos'
)

# 4. Calcular a Diferença (Quem sofre mais nulos?)
# Se o resultado for positivo, anulam mais para Vereador
tabela_comparativa['Diferença'] = tabela_comparativa['vereador'] - tabela_comparativa['prefeito']

print("Porcentagem de Votos Brancos + Nulos (Quem foi votar mas não escolheu ninguém):")
print(tabela_comparativa)

print("\n--- ANÁLISE ---")
media_diferenca = tabela_comparativa['Diferença'].mean()
if media_diferenca > 0:
    print(f"Resultado: Em média, o eleitor anula {media_diferenca:.1f}% a mais de votos para VEREADOR.")
else:
    print("Resultado: O eleitor anula mais para PREFEITO.")