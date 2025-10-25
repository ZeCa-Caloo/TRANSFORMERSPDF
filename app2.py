import streamlit as st, sys, subprocess, traceback

st.title("Diagnóstico do App ✅")

st.write("Python:", sys.version)
st.write("Executable:", sys.executable)

st.subheader("Pacotes instalados (pip freeze)")
try:
    freeze = subprocess.check_output([sys.executable, "-m", "pip", "freeze"], text=True, timeout=60)
    st.code(freeze)
except Exception as e:
    st.error(f"Falha no pip freeze: {e}")

st.subheader("Teste de imports críticos")
errors = []
for mod in ["Pillow", "pypdf", "reportlab", "mammoth", "xhtml2pdf"]:
    try:
        __import__(mod if mod != "Pillow" else "PIL")
        st.success(f"Import OK: {mod}")
    except Exception as e:
        errors.append((mod, str(e)))
        st.error(f"Import FALHOU: {mod} -> {e}")

if errors:
    st.warning("Alguns imports falharam. Corrija o requirements.txt / reinstale dependências e reexecute.")

st.subheader("Upload rápido para juntar PDFs (sanity check)")
from io import BytesIO
try:
    from pypdf import PdfMerger

    files = st.file_uploader("Envie 2+ PDFs para juntar (teste)", type=["pdf"], accept_multiple_files=True)
    if files and len(files) >= 2:
        merger = PdfMerger()
        for f in files:
            merger.append(BytesIO(f.read()))
        out = BytesIO()
        merger.write(out); merger.close()
        st.download_button("Baixar PDF unido", data=out.getvalue(), file_name="merged.pdf")
except Exception:
    st.exception(traceback.format_exc())
