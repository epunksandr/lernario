from supabase_folder.supabase_client_manager import SupabaseClientManager

def login_user(email, password):
    try:
        client = SupabaseClientManager.get_client()
        auth_response = client.auth.sign_in_with_password({
            'email': email,
            'password': password
        })

        # auth_response enthält ein dict mit 'session' und 'user'
        if auth_response and auth_response.session:
            return {
                "email": auth_response.user.email,
                "user": auth_response.user,
                "access_token": auth_response.session.access_token
            }
        else:
            return None
    except Exception as e:
        print(f"Fehler bei der Anmeldung: {e}")
        return None
