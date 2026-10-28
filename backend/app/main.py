from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Minha API FastAPI",
    description="Exemplo de documentação automática com Swagger",
    version="1.0.0"
)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )