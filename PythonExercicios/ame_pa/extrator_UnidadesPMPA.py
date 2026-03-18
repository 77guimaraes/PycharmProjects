#Extrai dados dos arquivos em PDF da PMPA (Efetivos)

import os
import re
import pdfplumber
import pandas as pd

# 1. Indique o caminho da pasta onde estão todos os PDFs
pasta_pdfs = r"C:\EFETIVOS-PMPA-2026"

print("Iniciando leitura da pasta...")
print("Caminho:", pasta_pdfs)
print("Arquivos encontrados:", os.listdir(pasta_pdfs))

dados_extraidos = []

# 2. Padrões de busca (Regex) para encontrar as informações no texto
padrao_nome = re.compile(r"Nome:\s*(.*)")
padrao_guerra = re.compile(r"Nome de guerra:\s*(.*)")
padrao_rg = re.compile(r"RG:\s*(.*)")
padrao_mf = re.compile(r"MF:\s*(.*)")
padrao_celular = re.compile(r"Celular:\s*(.*)")
padrao_celular2 = re.compile(r"Celular2:\s*(.*)")

# 3. Varrer todos os ficheiros PDF da pasta
for ficheiro in os.listdir(pasta_pdfs):
    print("Processando:", ficheiro)
    if ficheiro.lower().endswith(".pdf"):
        caminho_completo = os.path.join(pasta_pdfs, ficheiro)

        with pdfplumber.open(caminho_completo) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if not texto:
                    continue

                # Dividir o texto da página em blocos individuais por cada militar
                blocos = texto.split("Nome: ")[1:]

                for bloco in blocos:
                    bloco_completo = "Nome: " + bloco

                    # Buscar as informações no bloco
                    nome = padrao_nome.search(bloco_completo)
                    guerra = padrao_guerra.search(bloco_completo)
                    rg = padrao_rg.search(bloco_completo)
                    mf = padrao_mf.search(bloco_completo)
                    celular = padrao_celular.search(bloco_completo)
                    celular2 = padrao_celular2.search(bloco_completo)

                    # Limpar os dados encontrados
                    nome_str = nome.group(1).strip() if nome else ""
                    guerra_str = guerra.group(1).strip() if guerra else ""
                    rg_str = rg.group(1).strip() if rg else ""
                    mf_str = mf.group(1).strip() if mf else ""
                    cel1_str = celular.group(1).strip() if celular else ""
                    cel2_str = celular2.group(1).strip() if celular2 else ""

                    # Juntar os telefones
                    telefone = cel1_str
                    if cel2_str:
                        telefone += f" / {cel2_str}"

                    # Isolar a Graduação/Posto (Remove a última palavra do Nome de Guerra)
                    # Exemplo: "TEN CEL FREITAS" -> "TEN CEL"
                    partes_guerra = guerra_str.split()
                    graduacao = " ".join(partes_guerra[:-1]) if len(partes_guerra) > 1 else guerra_str

                    dados_extraidos.append({
                        "NOME COMPLETO": nome_str,
                        "GRADUAÇÃO/POSTO": graduacao,
                        "CPF": "",  # Mantido vazio para preservar a estrutura exigida
                        "RG": rg_str,
                        "MF": mf_str,
                        "ENDEREÇO": "",  # Mantido vazio para preservar a estrutura exigida
                        "TELEFONE": telefone,
                        "UNIDADE": ficheiro.replace(".pdf", "")  # Identifica de qual BPM o dado veio
                    })

# 4. Criar a tabela e exportar para Excel
df = pd.DataFrame(dados_extraidos)
df.to_excel("Efetivo_Geral_PMPA_Consolidado.xlsx", index=False)
print(f"Extração concluída! {len(df)} militares processados. Ficheiro gerado com sucesso.")