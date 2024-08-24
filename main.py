import re

import pandas as pd
from docx import Document

doc = Document("Partnership.docx")

# Extrair todo o texto do documento
texto_contrato = ""
for paragrafo in doc.paragraphs:
    texto_contrato += paragrafo.text + "\n"

# Regex para extrair nome e quantidade de cotas
socios = re.findall(
    r"(\d+\.\s)([\w\s]+),\sportador(?:a)?\sdo\sCPF\s[\d\.\-]+,.*?detentor(?:a)?\sde\s(\d+)\s(cotas|cota)",
    texto_contrato,
)

# Formatando a saída como uma lista de dicionários
quadro_societario = [{"Nome": socio[1], "Cotas": int(socio[2])} for socio in socios]

# Cria a planilha
pd.DataFrame(quadro_societario).to_excel(
    "Quadro societário.xlsx", index=False, sheet_name="Sócios e cotas"
)

print("Planilha criada")
