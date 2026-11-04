from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.payroll import Company, Employee
from app.schemas import CompanyModel, CompanyResponse, EmployeeModel, EmployeeResponse

router = APIRouter()


@router.post(
    "/companies", tags=["companies"], response_model=CompanyResponse, status_code=201
)
def create_company(company: CompanyModel, db: Annotated[Session, Depends(get_db)]):
    new_company = Company(**company.model_dump())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)

    return new_company


@router.get("/companies", response_model=list[CompanyResponse])
def get_all_companies(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Company))
    items = result.scalars().all()
    return items


@router.post(
    "/employees", tags=["employees"], response_model=EmployeeResponse, status_code=201
)
def create_employee(employee: EmployeeModel, db: Annotated[Session, Depends(get_db)]):
    new_employee = Employee(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@router.get("/employees", response_model=list[EmployeeResponse])
def get_all_employees(db: Annotated[Session, Depends(get_db)]):
    result = db.execute(select(Employee))
    items = result.scalars().all()
    return items
