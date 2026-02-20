import requests
import pandas as pd
from datetime import datetime

# =========== E - Extraction API de Cambio ============
url = "https://economia.awesomeapi.com.br/last/USD-BRL"

try:
    response = requests.get(url)
    dados = response.json()

    # ========== T - Transformation ===========
    # Pegamos o valor de compra (BID)
    cotacao_usd = float(dados['USDBRL']['bid'])
    data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')

    df_cambio = pd.DataFrame({
        'Moeda':['Dólar'],
        'Taxa':[cotacao_usd],
        'Ultima_atualizacao':[data_atual]
    })

    # ======== L - Load (carga) =============
    df_cambio.to_csv('data/cotacao_atual.csv', index=False,decimal='.')
    print(f"ETL Cambio concluido, Dolar Hoje: R$ {cotacao_usd}")

except Exception as e:
    print(f"Erro ao tentar cambio {e}")