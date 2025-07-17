# ChatJus RAG – Assistente Jurídico com LangChain e eProc

Este projeto é um assistente jurídico baseado em RAG (Retrieval-Augmented Generation) usando **LangChain**, **Elasticsearch** e **decisões extraídas do eProc**.

---

## 📂 Estrutura do Projeto

```
chatjus_rag_project/
├── .env.example                 # Exemplo com chave da OpenAI
├── requirements.txt            # Dependências do projeto
├── streamlit_app.py            # Interface de consulta via navegador
├── data/
│   └── decisoes.csv            # Decisões judiciais simuladas do eProc
└── backend/
    ├── vectorize.py            # Vetorização e indexação no Elasticsearch
    └── rag_agent.py            # Pipeline RAG com LangChain
```

---

## 🚀 Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure a variável de ambiente:
```bash
cp .env.example .env
```

3. Inicie o Elasticsearch localmente na porta 9200.

4. Indexe as decisões:
```bash
python backend/vectorize.py
```

5. Rode a interface Streamlit:
```bash
streamlit run streamlit_app.py
```

---

## 🧠 Tecnologias utilizadas

- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4](https://platform.openai.com/)
- [Elasticsearch](https://www.elastic.co/)
- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)

---

## 📌 Observação

O conteúdo em `data/decisoes.csv` é simulado apenas para demonstração. Para uso real, recomenda-se extração da base eProc via banco, web scraping autorizado ou APIs públicas do Judiciário.

---

## 🔒 Segurança

**Não compartilhe sua `OPENAI_API_KEY` publicamente.** Use variáveis de ambiente seguras e um arquivo `.env` local.

---

Criado por Anderson • Projeto piloto de IA aplicada ao Judiciário.
