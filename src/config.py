from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    mode: str = "DEV"
    
    db_user: str
    db_pass: str
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def is_dev(self) -> bool:
        return self.mode == "DEV"

    @property
    def is_test(self) -> bool:
        return self.mode == "TEST"


settings = Settings()
