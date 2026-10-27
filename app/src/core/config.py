from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = (
    "AppConfigDC",
    "ElasticConfigDC",
    "RedisConfigDC",
)


class RedisConfigDC(BaseModel):
    host: str = Field("localhost", alias="HOST")
    port: int = Field(6379, alias="PORT")
    password: str | None = Field(None, alias="PASSWORD")
    db: int = Field(0, alias="DB")
    decode_responses: bool = Field(True, alias="DECODE_RESPONSES")


class ElasticConfigDC(BaseModel):
    host: str = Field("localhost", alias="HOST")
    port: int = Field(9200, alias="PORT")


class AppConfigDC(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_nested_delimiter="__",
        env_file=".env.app.local",
    )
    host: str = Field("localhost", alias="APP_HOST")
    port: int = Field(8000, alias="APP_PORT")
    project_name: str = Field("Project", alias="APP_PROJECT_NAME")
    log_level: str = Field("INFO", alias="APP_LOG_LEVEL")
    entrypoint: str = Field("app:main", alias="APP_ENTRYPOINT")
    redis: RedisConfigDC = Field(alias="REDIS")
    elastic: ElasticConfigDC = Field(alias="ELASTIC")
    description: str = Field("", alias="APP_DESCRIPTION")
