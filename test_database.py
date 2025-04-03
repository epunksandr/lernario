from flask import Flask, jsonify
from supabase import create_client, Client

app = Flask(__name__)

# Deine Supabase-URL und API-Schlüssel
SUPABASE_URL = "https://your-project.supabase.co"  # Ersetze dies mit deiner Supabase URL
SUPABASE_KEY = "your-supabase-api-key"  # Ersetze dies mit deinem API-Schlüssel

# Supabase-Client erstellen
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def check_connection():
    try:
        # Eine einfache Abfrage auf einer Tabelle durchführen (z.B. 'users')
        response = supabase.table('users').select('*').execute()

        # Wenn die Abfrage erfolgreich ist, gib die Daten oder eine Erfolgsmeldung zurück
        if response.status_code == 200:
            return jsonify({"message": "Verbindung zu Supabase erfolgreich!", "data": response.data})
        else:
            return jsonify({"error": "Fehler bei der Verbindung zu Supabase", "details": response.error}), 500

    except Exception as e:
        # Fehler bei der Verbindung abfangen und eine Nachricht zurückgeben
        return jsonify({"error": "Fehler bei der Verbindung zu Supabase", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)