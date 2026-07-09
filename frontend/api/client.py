import requests

BASE_URL = "http://127.0.0.1:8000"


def get_documents():
    response = requests.get(
        f"{BASE_URL}/documents"
    )
    return response.json()


def get_stats():
    response = requests.get(
        f"{BASE_URL}/stats"
    )

    response.raise_for_status()

    return response.json()


def query(question: str):
    response = requests.post(
        f"{BASE_URL}/query",
        json={
            "question": question
        }
    )
    return response.json()


def delete_document(filename: str):
    response = requests.delete(
        f"{BASE_URL}/documents/{filename}"
    )
    return response.json()

def ingest_document(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    response = requests.post(
        f"{BASE_URL}/ingest",
        files=files
    )

    return response

