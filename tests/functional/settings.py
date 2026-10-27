from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

__all__ = (
    "LOG_SETTINGS",
    "AppConfigDC",
    "ElasticConfigDC",
    "RedisConfigDC",
    "TestConfigDC",
    "test_config",
)


class ElasticConfigDC(BaseModel):
    host: str = Field("localhost", alias="HOST")
    port: int = Field(9200, alias="PORT")
    indexes: list[str] = Field(default_factory=list, alias="INDEXES")


class RedisConfigDC(BaseModel):
    host: str = Field("localhost", alias="HOST")
    port: int = Field(6379, alias="PORT")
    password: str = Field("redispass", alias="PASSWORD")


class AppConfigDC(BaseModel):
    host: str = Field("localhost", alias="HOST")
    port: int = Field(8000, alias="PORT")


class TestConfigDC(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_nested_delimiter="__",
        env_file=".env.test.local",
    )

    app: AppConfigDC = Field(alias="APP")
    elastic: ElasticConfigDC = Field(alias="ELASTIC")
    redis: RedisConfigDC = Field(alias="REDIS")


LOG_SETTINGS = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(levelname)s - [%(module)s.%(funcName)s] - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "tests": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        }
    },
    "root": {"level": "WARNING", "handlers": ["console"]},
}

test_config = TestConfigDC()
