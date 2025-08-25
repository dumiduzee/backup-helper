from supabase import create_client,Client
from .settings import settings

url : str = settings.SUPABASE_URL
key : str = settings.SUPABASE_KEY

#supabase client initializing
supabase : Client = create_client(url,key)

def get_db():
    try:
        yield supabase
    finally:
        pass