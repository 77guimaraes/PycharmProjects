import pandas as pd

# ===== 1. CARREGAR ARQUIVOS =====
efetivo = pd.read_excel("Efetivo_Geral_PMPA_2026.xlsx")
referencia = pd.read_excel("Unidades_PMPA_Cidades.xlsx")

# ===== 2. PADRONIZAR NOMES DAS COLUNAS =====
efetivo.columns = efetivo.columns.str.strip().str.upper()
referencia.columns = referencia.columns.str.strip().str.upper()

# ===== 3. LIMPAR OS DADOS (tipo ARRUMAR do Excel) =====
efetivo["UNIDADES"] = efetivo["UNIDADES"].astype(str).str.strip().str.upper()
referencia["UNIDADES"] = referencia["UNIDADES"].astype(str).str.strip().str.upper()

# ===== 4. FAZER O CRUZAMENTO =====
resultado = efetivo.merge(referencia, on="UNIDADES", how="left")

# ===== 5. RENOMEAR COLUNA (pra ficar organizado) =====
resultado.rename(columns={"CIDADES_y": "CIDADE"}, inplace=True)

# (se existir CIDADES_x, pode remover)
if "CIDADES_x" in resultado.columns:
    resultado.drop(columns=["CIDADES_x"], inplace=True)

# ===== 6. SALVAR RESULTADO =====
resultado.to_excel("Efetivo_Com_Cidades.xlsx", index=False)

print("Arquivo criado com sucesso!")