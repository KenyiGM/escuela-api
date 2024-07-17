import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    secret_key   : str
    database_url : str
    debug        : bool

    class Config:
        env_file = ".env"

settings = Settings()
