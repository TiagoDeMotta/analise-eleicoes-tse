import pandas as pd

# Configurações para exibir os números bonitos (sem notação científica)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.0f}'.format

print("--- ANALISANDO DUQUE DE CAXIAS (RJ) ---\n")

arquivo = "br_tse_eleicoes_detalhes_votacao_municipio.csv"
df = pd.read_csv(arquivo)

# 1. FILTRAGEM: Apenas Duque de Caxias (3301702) e apenas 1º Turno
# Focamos no 1º turno porque é onde todos os candidatos concorrem
filtro_caxias = (df['id_municipio'] == 3301702) & (df['turno'] == 1) & (df['cargo'] == 'prefeito')
caxias = df[filtro_caxias].copy()

# 2. SELEÇÃO DE COLUNAS: Vamos pegar só o que importa
colunas_importantes = ['ano', 'aptos', 'comparecimento', 'abstencoes', 'votos_validos', 'votos_brancos', 'votos_nulos']
tabela = caxias[colunas_importantes].sort_values(by='ano')

# 3. CRIANDO NOVAS COLUNAS (Engenharia de Dados)
# Vamos calcular a % de Abstenção (quem faltou)
tabela['% Abstenção'] = (tabela['abstencoes'] / tabela['aptos']) * 100

# Vamos calcular a % de Votos "Perdidos" (Brancos + Nulos)
tabela['% Brancos/Nulos'] = ((tabela['votos_brancos'] + tabela['votos_nulos']) / tabela['comparecimento']) * 100

# Ajustando a formatação para leitura fácil
tabela['% Abstenção'] = tabela['% Abstenção'].map('{:.1f}%'.format)
tabela['% Brancos/Nulos'] = tabela['% Brancos/Nulos'].map('{:.1f}%'.format)

# 4. EXIBINDO O RESULTADO FINAL
print(tabela[['ano', 'aptos', 'comparecimento', '% Abstenção', '% Brancos/Nulos']].to_string(index=False))

print("\n--- CONCLUSÃO RÁPIDA ---")
ultimo_ano = tabela.iloc[-1]
print(f"Na última eleição registrada ({ultimo_ano['ano']}), Caxias tinha {ultimo_ano['aptos']} eleitores.")