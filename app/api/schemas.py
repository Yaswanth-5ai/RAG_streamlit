from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str

class IngestResponse(BaseModel):
    message: str
    filename: str