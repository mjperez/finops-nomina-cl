from fastapi import FastAPI

from app.api.v1.payroll import router

app = FastAPI(docs_url="/api/docs")


@app.get("/health")
async def read_health():
    return {"status": "ok", "service": "finops-nomina-cl"}


app.include_router(router, prefix="/api/v1")

