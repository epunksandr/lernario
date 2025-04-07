from supabase_folder.supabase_client_manager import SupabaseClientManager

def login_user(email, password):
    try:
        user = SupabaseClientManager.get_client().auth.sign_in_with_password({
            'email': email,
            'password': password
        })
        print(f"Benutzer angemeldet: {user}")
    except Exception as e:
        print(f"Fehler bei der Anmeldung: {e}")

def get_current_user():
    user = SupabaseClientManager.get_client().auth.get_user()
    if user:
        print(f"Eingeloggter Benutzer: {user}")
    else:
        print("Kein Benutzer eingeloggt")
