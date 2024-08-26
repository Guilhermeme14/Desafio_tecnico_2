import re

import pandas as pd
from docx import Document


def extrair_texto_docx(caminho_arquivo):
    # Extrai todo o texto de um documento DOCX.
    try:
        doc = Document(caminho_arquivo)
        texto = ""
        for paragrafo in doc.paragraphs:
            texto += paragrafo.text + "\n"
        return texto
    except FileNotFoundError as e:
        print(f"Erro ao abrir o arquivo DOCX: {e}")
        raise
    except Exception as e:
        print(f"Erro inesperado ao extrair texto do DOCX: {e}")
        raise


def extrair_socios(texto):
    # Extrai os nomes dos sócios e a quantidade de cotas do texto usando regex.
    try:
        socios = re.findall(
            r"(\d+\.\s)([\w\s]+),\sportador(?:a)?\sdo\sCPF\s[\d\.\-]+,.*?detentor(?:a)?\sde\s(\d+)\s(cotas|cota)",
            texto,
        )
        quadro_societario = [
            {"Nome": socio[1], "Cotas": int(socio[2])} for socio in socios
        ]
        return quadro_societario
    except re.error as e:
        print(f"Erro ao aplicar regex: {e}")
        raise
    except Exception as e:
        print(f"Erro inesperado ao extrair sócios: {e}")
        raise


def criar_planilha_socios(quadro_societario, arquivo_novo):
    # Cria uma planilha Excel com os dados do quadro societário.
    try:
        df = pd.DataFrame(quadro_societario)
        df.to_excel(arquivo_novo, index=False, sheet_name="Sócios e cotas")
        print(f"Planilha criada: {arquivo_novo}")
    except Exception as e:
        print(f"Erro inesperado ao criar planilha: {e}")
        raise
