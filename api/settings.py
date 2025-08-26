from pydantic_settings import BaseSettings
from decouple import config

class Settings(BaseSettings):
    SUPABASE_URL :str =  config("SUPABASE_URL")
    SUPABASE_KEY :str = config("SUPABASE_KEY")
    ADMIN_MOBILE : str = config("ADMIN_MOBILE")
    BASE_URL : str = config("BASE_URL")
    API_TOKEN :str = config("API_TOKEN")
    SENDER_ID :str = config("SENDER_ID")


settings = Settings()