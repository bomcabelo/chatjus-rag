import streamlit as st
from backend.rag_agent import responder_pergunta

st.set_page_config(page_title="Assistente Jurídico eProc", layout="wide")
st.title("📚 Assistente Jurídico – RAG com LangChain")

pergunta = st.text_area("Digite sua dúvida jurídica:", height=150)

if st.button("Consultar"):
    with st.spinner("Buscando decisões..."):
        resposta, fontes = responder_pergunta(pergunta)

    st.markdown("### ✅ Resposta")
    st.write(resposta)

    st.markdown("### 📄 Fontes utilizadas")
    for i, doc in enumerate(fontes):
        st.markdown(f"**{i+1}. Processo**: `{doc.metadata['processo']}`")
        st.markdown(f"```
{doc.page_content[:700]}...
```")
