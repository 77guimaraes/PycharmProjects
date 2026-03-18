#Extrai informações e gera um arquivo CSV contendo os endereços das unidades da PMPA diretamente do site da PMPA
#Versão que utilizei, pois extrai informações mais compatíveis com o que está contido no site

import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.pm.pa.gov.br/orgaos-de-execucao.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

texto = soup.get_text("\n")
linhas = texto.split("\n")

dados = []
unidade_atual = None
vistos = set()  # evita duplicados


# 📌 Função MELHORADA para extrair cidade
def extrair_cidade(unidade, endereco):
    texto = (unidade + " " + endereco).upper()

    # ✅ 1. padrão: Cidade - PA ou Cidade/PA
    match = re.search(r'([A-ZÀ-ÿ\s]+)[-/]\s*PA', texto)
    if match:
        cidade = match.group(1).strip()

        # remove palavras lixo
        lixo = ["BAIRRO", "CEP", "RUA", "AV", "ROD", "KM"]
        if not any(p in cidade for p in lixo):
            return cidade

    # ✅ 2. cidade dentro de parênteses na unidade
    match2 = re.search(r'\(([^)]+)\)', unidade)
    if match2:
        return match2.group(1).strip().upper()

    # ❌ 3. não encontrou nada confiável
    return ""


for linha in linhas:
    linha = linha.strip()

    if not linha:
        continue

    # 👉 Detecta unidade
    if (
        "BPM" in linha
        or "CIPM" in linha
        or "BATALHÃO" in linha
        or "COMPANHIA" in linha
    ):
        unidade_atual = linha

    # 👉 Detecta endereço
    elif linha.lower().startswith("endereço"):
        endereco = linha.split(":", 1)[-1].strip()

        cidade = extrair_cidade(unidade_atual, endereco)

        # cria chave única pra evitar duplicados
        chave = (unidade_atual, endereco)

        if unidade_atual and endereco and chave not in vistos:
            vistos.add(chave)

            dados.append({
                "unidade": unidade_atual,
                "endereco": endereco,
                "cidade": cidade
            })


# 💾 Salvar CSV
with open("unidades_pmpa_limpo.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["unidade", "endereco", "cidade"])
    writer.writeheader()
    writer.writerows(dados)

print("✅ CSV LIMPO gerado com sucesso!")