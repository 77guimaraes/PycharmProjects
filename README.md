Pasta ame_pa > extrator_pmpa.py:
O projeto "extrator_pmpa", utilizando as bibliotecas "pandas" e "pdfplumber" tem a finalidade extrair dados de arquivos em PDF e organizá-los em um arquivos .xlsx. Etapas do programa:
    1. Abre a pasta onde estão os PDF's das unidades da PMPA, sendo um arquivo por unidade, totalizando 184 unidades militares;
    2. Lê o documentos para encontrar as seguintes informações: NOME COMPLETO, GRADUAÇÃO/POSTO, CPF, RG, MF (Matrícula Funcional), ENDEREÇO, TELEFONE e UNIDADE;
    3. Guarda as inforamções encontradas;
    4. Cola as informações encontradas em uma planilha (arquivo em formato .xlsx).

Em 10 minutos foram extraídos dados de 17.992 militares.
