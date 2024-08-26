from extrair import *


def main():
    caminho_arquivo = "data/Partnership.docx"
    texto_contrato = extrair_texto_docx(caminho_arquivo)
    quadro_societario = extrair_socios(texto_contrato)
    criar_planilha_socios(quadro_societario, "data/Quadro societário.xlsx")


if __name__ == "__main__":
    main()
