from supabase_folder.supabase_client_manager import SupabaseClientManager


def loesche_schueler(id: int):
    supabase = SupabaseClientManager.get_client()

    supabase.table("students").delete().eq("id", id).execute()

def gib_alle_schueler_mit_grundinformationen():
    supabase = SupabaseClientManager.get_client()
    response = supabase.rpc("gib_alle_schueler_mit_grundinformationen", {}).execute()
    return response.data