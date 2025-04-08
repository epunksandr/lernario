from supabase_folder.supabase_client_manager import SupabaseClientManager

def do(): 
    response = SupabaseClientManager.get_client().table('users').select('*').execute()

    print("")
    print("")
    print("")
    print("")
    print("")
    print(response)