documents = get_documents()
stats = get_stats()


with st.sidebar:

    st.header("📊 Stats")

    st.metric(
        "Documents",
        stats["documents"]
    )

    st.metric(
        "Chunks",
        stats["chunks"]
    )

    st.divider()

    st.header("📂 Documents")

    st.subheader("⬆ Upload New Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if uploaded_file:

        with st.spinner(
            "Uploading and indexing document..."
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
                    response.json()["detail"]
                )

    st.divider()

    for doc in documents:

        col1, col2 = st.columns([4,1])

        with col1:
            st.write(
                f"📄 {doc['document_name']}"
            )

        with col2:

            if st.button(
                "🗑️",
                key=f"delete_{doc['document_name']}"
            ):

                delete_document(
                    doc["document_name"]
                )

                st.rerun()