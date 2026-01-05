import pandas as pd
import matplotlib.pyplot as plt

# Configuração de Estilo Limpo
plt.rcParams['font.family'] = 'sans-serif'
# Tenta usar Arial, se não tiver, usa a padrão do sistema
try:
    plt.rcParams['font.sans-serif'] = ['Arial']
except:
    pass

print("--- GERANDO GRÁFICO SOCIAL ---")

arquivo = "br_tse_eleicoes_detalhes_votacao_municipio.csv"
try:
    df = pd.read_csv(arquivo)
except FileNotFoundError:
    print(f"ERRO: O arquivo '{arquivo}' não foi encontrado na pasta.")
    exit()

# 1. PREPARAR DADOS
# Filtra Caxias (3301702) e 1º Turno
filtro = (df['id_municipio'] == 3301702) & (df['turno'] == 1)
caxias = df[filtro].copy()

# Calcula a porcentagem de rejeição
caxias['% Rejeicao'] = ((caxias['votos_brancos'] + caxias['votos_nulos']) / caxias['comparecimento']) * 100

# CORREÇÃO AQUI: Pivotar e selecionar APENAS as colunas que importam antes de limpar
dados = caxias.pivot_table(index='ano', columns='cargo', values='% Rejeicao')

# Verifica se as colunas existem antes de tentar acessar
if 'prefeito' not in dados.columns or 'vereador' not in dados.columns:
    print("ERRO: Não encontrei dados suficientes de Prefeito e Vereador para comparar.")
    print("Colunas encontradas:", dados.columns)
    exit()

# Agora selecionamos só as duas e limpamos os anos que não têm as duas
dados = dados[['prefeito', 'vereador']].dropna()

print("Anos encontrados para o gráfico:", list(dados.index))

if dados.empty:
    print("ERRO: A tabela ficou vazia após o filtro. Verifique os dados.")
    exit()

# 2. CRIAR O GRÁFICO
plt.figure(figsize=(10, 8), dpi=150)

# Remover bordas desnecessárias
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 3. PLOTAR AS LINHAS
plt.plot(dados.index, dados['prefeito'], color='#D32F2F', linewidth=4, marker='o')
plt.plot(dados.index, dados['vereador'], color='#7F8C8D', linewidth=3, linestyle='--', marker='o')

# 4. RÓTULOS DIRETOS
ult_ano = dados.index[-1]
val_pref = dados['prefeito'].iloc[-1]
val_ver = dados['vereador'].iloc[-1]

plt.text(ult_ano + 0.5, val_pref, f'PREFEITO\n({val_pref:.1f}%)', color='#D32F2F', fontweight='bold', va='center')
plt.text(ult_ano + 0.5, val_ver, f'Vereador\n({val_ver:.1f}%)', color='#7F8C8D', fontweight='bold', va='center')

# 5. DESTAQUE E ANOTAÇÕES
plt.fill_between(dados.index, dados['prefeito'], dados['vereador'],
                 where=(dados['prefeito'] > dados['vereador']),
                 color='#D32F2F', alpha=0.1)

# Anotação (só adiciona se o ano 2016 existir nos dados para não dar erro)
if 2016 in dados.index:
    plt.annotate('AQUI MUDOU TUDO\n(2016)',
                 xy=(2016, dados.loc[2016, 'prefeito']),
                 xytext=(2010, 20), # Ajustei a altura para não cortar
                 arrowprops=dict(facecolor='black', arrowstyle='->', lw=2),
                 fontsize=10, fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="none", alpha=0.3))

# 6. TÍTULOS
plt.title('Quem o eleitor de Caxias\nrejeita mais nas urnas?', fontsize=18, fontweight='bold', loc='left')
plt.ylabel('% de Votos Brancos e Nulos', fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

nome_arquivo = 'post_instagram_caxias.png'
plt.savefig(nome_arquivo)
print(f"✅ SUCESSO! Gráfico salvo como: {nome_arquivo}")