from supabase import create_client
from supabase_folder import supabase_config

#Das ist ein Singleton
class SupabaseClientManager:
    _supabase_client = None

    @classmethod
    def get_client(cls):
        if cls._supabase_client is None:
            SUPABASE_URL = supabase_config.SUPABASE_URL
            SUPABASE_KEY = supabase_config.SUPABASE_KEY
            cls._supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return cls._supabase_client