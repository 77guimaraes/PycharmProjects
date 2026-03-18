#Extrai dados do PDF gerado na página dos Órgãos de Execução da PMPA

import pdfplumber

caminho_pdf = "orgaos_exec_pmpa.pdf"

dados = []  # Aqui vamos guardar unidade + endereço

with pdfplumber.open(caminho_pdf) as pdf:
    for pagina in pdf.pages:
        texto = pagina.extract_text()

        if not texto:
            continue

        linhas = texto.split("\n")  # quebra o texto em linhas

        unidade_atual = None

        for linha in linhas:
            linha = linha.strip()

            # 👉 Identifica possível nome de unidade
            if (
                    "BATALHÃO" in linha
                    or "BPM" in linha
                    or "CIPM" in linha
                    or "CIME" in linha
            ):
                unidade_atual = linha

            # 👉 Identifica endereço
            if linha.startswith("Endereço:"):
                endereco = linha.replace("Endereço:", "").strip()

                if unidade_atual:
                    dados.append({
                        "unidade": unidade_atual,
                        "endereco": endereco
                    })

# 👉 Mostra resultado
for item in dados:
    print(item)