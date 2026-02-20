import subprocess
import time
import os

def limpar_arquivos_antigos():
    # Remoçao de arquivos antigos do diretorio /data para evitar conflitos
    arquivos_para_remover = [
        'data/cotacao_atual.csv',
        'data/vendas_final.csv',
    ]
    print("Limpando arquivos residuais...")
    for arquivo in arquivos_para_remover:
        if os.path.exists(arquivo):
            try:
                os.remove(arquivo)
                print(f"  -{arquivo} removido com sucesso!")
            except PermissionError:
                print(f"Não foi possível remover o arquivo {arquivo}!")

def executar_pipeline():
    print("Iniciando pipeline de dados completos...")
    inicio = time.time()

    try:
        print("\n[1/2] Processando vendas...")
        subprocess.run(["python", "scripts/pipeline_csv.py"], check=True)

        print("\n[2/2] Buscando câmbio...")
        subprocess.run(["python", "scripts/pipeline_cambio.py"], check=True)

        fim = time.time()

        print(f"\n Sucesso em {round(fim - inicio, 2)} segundos!")

    except subprocess.CalledProcessError as e:
        print(f"Erro: O script{e.cmd} falhou")

if __name__ == "__main__":
    executar_pipeline()