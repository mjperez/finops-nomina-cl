from fastapi import FastAPI

app = FastAPI(docs_url="/api/docs")


@app.get("/health")
async def read_health():
    return {"status": "ok", "service": "finops-nomina-cl"}
