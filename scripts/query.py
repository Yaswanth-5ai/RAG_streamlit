from app.query.query_pipeline import QueryPipeline


def main():

    pipeline = QueryPipeline()

    while True:

        query = input("\nAsk a question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        answer = pipeline.run(query)

        print("\n================ ANSWER ================\n")
        print(answer)


if __name__ == "__main__":
    main()