from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)

    rut_num: Mapped[int] = mapped_column(unique=True)

    rut_dv: Mapped[str] = mapped_column(String(1))

    razon_social: Mapped[str]

    nomina_name: Mapped[str]

    mutualidad_code: Mapped[str]

    accident_rate: Mapped[Decimal] = mapped_column(Numeric(5, 2))

    ccaf_code: Mapped[str | None]


class Employee(Base):
    __tablename__ = "employees"
    __table_args__ = (
        UniqueConstraint(
            "company_id", "rut_num"
        ),  # no se puede registrar dos veces el mismo rut dentro de la misma empresa
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))

    rut_num: Mapped[int]

    rut_dv: Mapped[str] = mapped_column(String(1))

    full_name: Mapped[str]

    base_salary_clp: Mapped[int]

    afp_code: Mapped[str]

    health_code: Mapped[str]

    contract_type: Mapped[str]
