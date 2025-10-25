# HTMLPDF Converter (Streamlit)

App em Python/Streamlit para converter HTML, Excel (.xls/.xlsx), DOCX e imagens (jpg/png/gif/bmp/tiff/webp/svg) para PDF.
Suporta unir múltiplos PDFs em um único arquivo.

## Como rodar (Windows)

1. Abra o PowerShell na pasta do projeto
2. Crie a venv e ative:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
4. Inicie o app:
   ```powershell
   streamlit run app\app.py
   ```

> Se WeasyPrint der erro de cairo/pango, selecione **xhtml2pdf** no app.

## Estrutura
```
HTMLPDF_full_package/
├─ app/
│  ├─ app.py
│  └─ saidas/
├─ requirements.txt
├─ pyproject.toml
└─ README.md
```
