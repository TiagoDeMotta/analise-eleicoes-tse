import pandas as pd
import matplotlib.pyplot as plt

# Configuração visual
plt.style.use('ggplot')

print("--- RAIO-X DEMOGRÁFICO: DUQUE DE CAXIAS (IBGE) ---")

# CAMINHO EXATO (Com o nome duplo .csv.csv)
arquivo = r"C:\Users\DEMOTTA\Documents\PROJETOS PYTHON\ibge_caxias.csv.csv"

try:
    # Lendo o arquivo (encoding latin1 é padrão do IBGE)
    df = pd.read_csv(arquivo, sep=';', encoding='utf-8', low_memory=False)
    print(f"✅ Arquivo carregado com sucesso!")
except FileNotFoundError:
    print(f"❌ ERRO: Ainda não achei. Confirme se o caminho é exatamente este:\n{arquivo}")
    exit()
except Exception as e:
    print(f"❌ Erro ao ler: {e}")
    exit()

# --- ANÁLISE ---

# 1. FILTRAR DUQUE DE CAXIAS
caxias = df[df['NM_MUN'].str.upper() == 'DUQUE DE CAXIAS'].copy()

# 2. RENOMEAR COLUNAS
# v0001 = População (Pessoas)
# v0002 = Domicílios (Casas)
caxias.rename(columns={'v0001': 'Populacao', 'v0002': 'Domicilios', 'NM_DIST': 'Distrito'}, inplace=True)

# 3. AGRUPAR POR DISTRITO
resumo = caxias.groupby('Distrito')['Populacao'].sum().sort_values(ascending=False)
porcentagem = (resumo / resumo.sum()) * 100

print("\n🏆 RANKING: Onde mora a população de Caxias?")
tabela_final = pd.DataFrame({'População': resumo, '% do Total': porcentagem.map('{:.1f}%'.format)})
print(tabela_final)

# 4. GERAR GRÁFICO DE PIZZA
plt.figure(figsize=(10, 8))
cores = ['#2980b9', '#e74c3c', '#f39c12', '#27ae60'] # Azul, Vermelho, Laranja, Verde

def rotulo_pizza(pct, allvals):
    absolute = int(pct/100.*sum(allvals))
    return "{:.1f}%\n({:,})".format(pct, absolute).replace(',', '.')

plt.pie(resumo, labels=resumo.index, autopct=lambda pct: rotulo_pizza(pct, resumo),
        startangle=90, colors=cores, explode=(0.05, 0, 0, 0), shadow=True)

plt.title('Divisão da População de Duque de Caxias\n(Por Distrito - Censo IBGE)', fontsize=14, fontweight='bold')
plt.tight_layout()

plt.savefig('analise_distritos.png')
print("\n✅ Gráfico salvo como: analise_distritos.png")