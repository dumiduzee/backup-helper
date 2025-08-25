from pydantic_settings import BaseSettings
from decouple import config

class Settings(BaseSettings):
    SUPABASE_URL :str =  config("SUPABASE_URL")
    SUPABASE_KEY :str = config("SUPABASE_KEY")


settings = Settings()