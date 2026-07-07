from fastapi import FastAPI

from app.api.routes import router
from app.container.container import ApplicationContainer

app = FastAPI(
    title="Production RAG API",
    description="REST API for the Production RAG System",
    version="2.0.0"
)

# Create shared objects once
app.state.container = ApplicationContainer()

# Register routes
app.include_router(router)