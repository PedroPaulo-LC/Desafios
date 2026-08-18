from __future__ import annotations

import io
from pathlib import Path

import streamlit as st

from src.document_loader import extract_text
from src.oci_llm import answer_with_oci, is_configured
from src.rag import KnowledgeBase, build_context, chunk_text

st.set_page_config(page_title="CorpMind AI", page_icon="🤖", layout="wide")

st.title("CorpMind AI")
st.caption("Agente corporativo para consultar documentos internos com RAG + OCI Generative AI")

if "messages" not in st.session_state:
    st.session_state.messages = []


def load_default_documents():
    loaded = []
    docs_dir = Path(__file__).parent / "documents"
    for path in docs_dir.glob("*"):
        if path.is_file():
            with path.open("rb") as file:
                text = extract_text(file, path.name)
            loaded.append((path.name, text))
    return loaded


with st.sidebar:
    st.header("Base de conhecimento")
    st.write("Use os documentos de demonstração ou envie arquivos da sua empresa.")
    uploaded_files = st.file_uploader(
        "Adicionar documentos",
        accept_multiple_files=True,
        type=["pdf", "docx", "xlsx", "xls", "pptx", "md", "txt", "csv", "json", "html", "htm"],
    )
    st.divider()
    if is_configured():
        st.success("OCI Generative AI configurado")
    else:
        st.warning("OCI não configurado. A busca documental funciona, mas a resposta generativa requer as variáveis do .env.")

sources = load_default_documents()
for uploaded in uploaded_files:
    try:
        text = extract_text(io.BytesIO(uploaded.getvalue()), uploaded.name)
        sources.append((uploaded.name, text))
    except Exception as exc:
        st.error(f"Não foi possível ler {uploaded.name}: {exc}")

chunks = []
for source_name, source_text in sources:
    chunks.extend(chunk_text(source_text, source_name))

knowledge_base = KnowledgeBase(chunks)

with st.expander(f"Documentos carregados ({len(sources)})"):
    for source_name, _ in sources:
        st.write(f"- {source_name}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Faça uma pergunta sobre os documentos...")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    results = knowledge_base.search(question, top_k=4)
    context = build_context(results)

    if not results:
        answer = "Não encontrei informações relacionadas a essa pergunta nos documentos disponíveis."
    elif is_configured():
        try:
            answer = answer_with_oci(question, context)
        except Exception as exc:
            answer = f"Não foi possível consultar o OCI Generative AI: {exc}"
    else:
        source_names = sorted({chunk.source for chunk, _ in results})
        excerpts = "\n\n".join(f"**{chunk.source}:** {chunk.text[:420]}..." for chunk, _ in results[:2])
        answer = (
            "Encontrei conteúdo relevante, mas o OCI Generative AI ainda não está configurado. "
            "Após configurar as variáveis de ambiente, o agente transformará esse contexto em uma resposta conversacional.\n\n"
            f"{excerpts}\n\n**Fontes encontradas:** {', '.join(source_names)}"
        )

    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)
