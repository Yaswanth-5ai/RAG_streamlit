from app.ingestion.pipeline import IngestionPipeline


def main():
    pipeline = IngestionPipeline()
    pipeline.run()


if __name__ == "__main__":
    main()