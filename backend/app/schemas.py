from decimal import Decimal

from pydantic import BaseModel, ConfigDict, model_validator

from app.domain.chilean_rules import validar_rut


class CompanyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    rut_num: int
    rut_dv: str
    razon_social: str
    nomina_name: str
    mutualidad_code: str
    accident_rate: Decimal
    ccaf_code: str | None = None

    @model_validator(mode="after")
    def check_rut(self):
        if not validar_rut(self.rut_num, self.rut_dv):
            raise ValueError("Rut no es válido")
        return self


class CompanyResponse(CompanyModel):
    id: int


class EmployeeModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    company_id: int
    rut_num: int
    rut_dv: str
    full_name: str
    base_salary_clp: int
    afp_code: str
    health_code: str
    contract_type: str

    @model_validator(mode="after")
    def check_rut(self):
        if not validar_rut(self.rut_num, self.rut_dv):
            raise ValueError("Rut no es válido")
        return self


class EmployeeResponse(EmployeeModel):
    id: int
