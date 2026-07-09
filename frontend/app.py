import streamlit as st

from api.client import (
    get_documents,
    get_stats,
    ingest_document,
    delete_document,
    query
)

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    layout="wide"
)

# Fetch backend data
documents = get_documents()
stats = get_stats()

# ---------------- Sidebar ----------------
with st.sidebar:

    st.title("📊 Stats")

    st.metric(
        "Documents",
        stats["documents"]
    )

    st.metric(
        "Chunks",
        stats["chunks"]
    )

    st.caption(
        f"Embedding: {stats['embedding_model']}"
    )

    st.caption(
        f"LLM: {stats['llm_model']}"
    )

    st.divider()

    st.title("📂 Documents")

    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("Upload File"):

            with st.spinner(
                "Uploading and indexing..."
            ):

                response = ingest_document(
                    uploaded_file
                )

                if response.status_code == 200:

                    st.success(
                        "Document indexed successfully."
                    )

                    st.rerun()

                else:

                    st.error(
                        response.text
                    )

    st.divider()

    for doc in documents:

        with st.container():

            st.write(
                f"📄 {doc['document_name']}"
            )

            # Metadata
            if "total_chunks" in doc:
                st.caption(
                    f"📑 Chunks: {doc['total_chunks']}"
                )

            if "file_type" in doc:
                st.caption(
                    f"📂 Type: {doc['file_type']}"
                )

            if "ingested_at" in doc:
                st.caption(
                    f"🕒 {doc['ingested_at'][:10]}"
                )

            if st.button(
                "🗑 Delete",
                key=f"delete_{doc['document_name']}"
            ):

                delete_document(
                    doc["document_name"]
                )

                st.rerun()

            st.divider()

if st.button("🧹 Clear Chat"):

    st.session_state.messages = []

    st.rerun()


# ---------------- Main Chat Area ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Enterprise RAG Assistant")

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
question = st.chat_input(
    "Ask a question about your documents..."
)

if question:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(question)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = query(question)

            answer = response["answer"]

            st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )