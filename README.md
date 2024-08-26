# Projeto de Extração e Análise de Dados de Sócios

Este projeto visa extrair informações sobre sócios e suas cotas a partir de documentos DOCX e gerar uma planilha Excel com esses dados. Abaixo estão as instruções para configurar, executar e testar o projeto.

## Dependências

Este projeto requer as seguintes bibliotecas Python:

- `pandas`
- `python-docx`
- `unittest`

Instale as dependências usando `pip`:

```bash
pip install pandas python-docx
```

## Funcionalidades

### Extrair dados (`src/extrair.py`)

Este módulo é responsável por extrair dados com base no texto contido no documento DOCX. Ele realiza as seguintes operações:

- **`extrair_texto_docx(caminho_arquivo):`** Recebe o caminho de um arquivo DOCX e retorna o texto contido no documento.
- **`extrair_socios(texto):`** Recebe um texto e utiliza expressões regulares para extrair informações sobre sócios e suas cotas.
- **`criar_planilha_socios(quadro_societario, arquivo_novo):`** Recebe uma lista de dicionários com informações dos sócios e cria uma planilha Excel com esses dados.
- **`salvar_resultado(df, resultado, caminho_arquivo):`** Salva os resultados do cálculo em uma planilha Excel formatada.

### Executar (`src/main.py`)

Script principal para execução. Extrai o texto de um documento DOCX, processa as informações dos sócios e cria uma planilha Excel.
Para executar o script principal, utilize o seguinte comando:

```bash
python src/main.py
```

## Testes

### Teste extrair (`test/test_extrair.py`)

Contém testes unitários para as funções definidas em `src/extrair.py`.

Os testes são realizados usando o módulo unittest. Para executá-los, utilize o seguinte comando:

```bash
python -m unittest discover -s test
```

## Instruções de Uso

1. Coloque o arquivo DOCX que contém as informações dos sócios no diretório `data` e nomeie-o como `Partnership.docx`.
2. Execute o script principal `src/main.py` para processar o arquivo DOCX e gerar a planilha Excel.
3. Verifique o arquivo `data/Quadro societário.xlsx` para assegurar que os dados foram extraídos e salvos corretamente.
