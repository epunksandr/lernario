def safe_execute_return_success(operation):
    try:
        response = operation()
        if response.error:
            print("Fehler:", response.error)
            return False
    except Exception as e:
        print("Ausnahme beim Ausführen:", e)
        return False
    return True

def safe_execute_return_data_or_none(operation):
    try:
        response = operation()
        if response.error:
            print("Fehler:", response.error)
            return None
        return response.data
    except Exception as e:
        print("Ausnahme beim Ausführen:", e)
        return None
