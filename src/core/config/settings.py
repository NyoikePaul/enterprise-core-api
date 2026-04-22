import os

class Settings:
    def __init__(self):
        # App config
        self.APP_NAME = os.getenv("APP_NAME", "Enterprise Core API")
        self.DEBUG = os.getenv("DEBUG", "true").lower() == "true"

        # Database config
        self.POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
        self.POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
        self.POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
        self.POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
        self.POSTGRES_DB = os.getenv("POSTGRES_DB", "app_db")

def get_settings():
    return Settings()
