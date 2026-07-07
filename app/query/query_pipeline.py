class QueryPipeline:

    def __init__(
        self,
        retriever,
        prompt_builder,
        llm
    ):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm

    def run(self, query: str) -> str:

        documents = self.retriever.retrieve(query)

        prompt = self.prompt_builder.build_prompt(
            question=query,
            documents=documents
        )

        answer = self.llm.generate(prompt)

        return answer