import pandas as pd
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch, helpers

df = pd.read_csv("data/decisoes.csv")
model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
es = Elasticsearch("http://localhost:9200")

if not es.indices.exists(index="eproc-decisoes"):
    es.indices.create(index="eproc-decisoes", body={
        "mappings": {
            "properties": {
                "numero_processo": {"type": "keyword"},
                "orgao_julgador": {"type": "text"},
                "conteudo": {"type": "text"},
                "embedding": {"type": "dense_vector", "dims": 384}
            }
        }
    })

def indexar_documentos():
    documentos = []
    for i, row in df.iterrows():
        embedding = model.encode(row['conteudo']).tolist()
        doc = {
            "_index": "eproc-decisoes",
            "_id": row["numero_processo"],
            "_source": {
                "numero_processo": row["numero_processo"],
                "orgao_julgador": row["orgao_julgador"],
                "conteudo": row["conteudo"],
                "embedding": embedding
            }
        }
        documentos.append(doc)
    helpers.bulk(es, documentos)
    print(f"{len(documentos)} documentos indexados.")

if __name__ == "__main__":
    indexar_documentos()
