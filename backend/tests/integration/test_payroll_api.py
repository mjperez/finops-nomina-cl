from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from starlette.testclient import TestClient

from app.core.database import Base, get_db
from app.main import app

test_engine = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}, poolclass=StaticPool
)


TestingSessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=test_engine)

Base.metadata.create_all(bind=test_engine)


def override_get_db():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_create_and_get_company():
    response_post = client.post("/api/v1/companies",json={"rut_num":11111111, "rut_dv":"1", "razon_social":"razon_social", "nomina_name":"nomina_name","mutualidad_code":"mutualidad_code", "accident_rate": 999.99})
    response_get = client.get("/api/v1/companies")

    
    assert response_post.status_code == 201
    assert response_get.json()
    
def test_create_company_invalid_rut():
    response = client.post("/api/v1/companies",json={"rut_num":11111111, "rut_dv":"K", "razon_social":"razon_social", "nomina_name":"nomina_name","mutualidad_code":"mutualidad_code", "accident_rate": 999.99})
    assert response.status_code == 422

def test_create_and_get_employee():
    response_post = client.post("/api/v1/employees",json={"company_id":1,"rut_num":22060449, "rut_dv":"7", "full_name":"full_name", "base_salary_clp":1000000,"afp_code":"HABITAT", "health_code": "health_code", "contract_type":"HONORARIOS"})
    response_get = client.get("/api/v1/employees")

   
    assert response_post.status_code == 201
    assert response_get.json()