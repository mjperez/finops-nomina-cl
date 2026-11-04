from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")
    DATABASE_URL: str = "postgresql+psycopg://finops_user:finops_pass@localhost:5432/finops_nomina"
    
settings = Settings()