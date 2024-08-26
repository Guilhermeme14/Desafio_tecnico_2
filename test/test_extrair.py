import unittest
from unittest.mock import MagicMock, patch

from src.extrair import criar_planilha_socios, extrair_socios, extrair_texto_docx


class TestExtrairTextoDocx(unittest.TestCase):

    @patch("src.extrair.Document")
    def test_extrair_texto_docx(self, mock_document):
        # Simulando o retorno de paragraphs
        mock_paragraphs = [
            MagicMock(text="Primeiro parágrafo"),
            MagicMock(text="Segundo parágrafo"),
        ]
        mock_doc_instance = MagicMock()
        mock_doc_instance.paragraphs = mock_paragraphs
        mock_document.return_value = mock_doc_instance

        # Chamando a função com o mock
        texto = extrair_texto_docx("dummy_path")

        # Verificando se o texto foi extraído corretamente
        self.assertEqual(texto, "Primeiro parágrafo\nSegundo parágrafo\n")


class TestExtrairSocios(unittest.TestCase):

    def test_extrair_socios(self):
        texto = """
        1. João Silva, portador do CPF 123.456.789-00, detentor de 1000 cotas.
        2. Maria Oliveira, portadora do CPF 987.654.321-00, detentora de 500 cotas.
        """
        resultado_esperado = [
            {"Nome": "João Silva", "Cotas": 1000},
            {"Nome": "Maria Oliveira", "Cotas": 500},
        ]
        resultado = extrair_socios(texto)

        self.assertEqual(resultado, resultado_esperado)


class TestCriarPlanilhaSocios(unittest.TestCase):

    @patch("pandas.DataFrame.to_excel")
    def test_criar_planilha_socios(self, mock_to_excel):
        quadro_societario = [
            {"Nome": "João Silva", "Cotas": 1000},
            {"Nome": "Maria Oliveira", "Cotas": 500},
        ]

        # Teste para verificar se o método to_excel é chamado com os parâmetros corretos
        criar_planilha_socios(quadro_societario, "teste.xlsx")

        mock_to_excel.assert_called_once_with(
            "teste.xlsx", index=False, sheet_name="Sócios e cotas"
        )
