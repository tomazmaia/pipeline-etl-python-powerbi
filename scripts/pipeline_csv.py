import pandas as pd

# ======== E - Extraction ===============
df = pd.read_csv('../data/vendas_brutas.csv', sep=',', encoding='utf-8-sig')

# DEBUG colunas encontradas
# print("Colunas encontradas: ", df.columns.tolist())

# ======== T - Transformation ============
# Limpar espaços e padronizar nomes (Capitalize)
df.columns = df.columns.str.strip()

if 'Vendedor' in df.columns:
    df['Vendedor'] = df['Vendedor'].str.strip().str.title()

    # Converter valor para número (trocar vírgula por ponto)
    if not pd.api.types.is_numeric_dtype(df['Valor']):
        print("Tratando coluna Valor: removendo virgulas e convertendo...")
        df['Valor'] = df['Valor'].astype(str).str.replace(',','.')
    # converter para float de forma segura
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

    # Criar coluna de comissão (10%)
    df['Comissao'] = df['Valor'] * 0.10
    # ======= L - Load (Carga) ===============
    df.to_csv('vendas_final.csv', index=False, decimal='.')
    print("\n --- Visualização dos dados processados ---")
    print(df.head())
    print("ETL concluido: Arquivo 'vendas_final.csv' gerado com sucesso!")
else:
    print(f"Erro: A coluna 'Vendedor' não foi encontrada. As colunas disponíveis são: {df.columns.tolist()}")