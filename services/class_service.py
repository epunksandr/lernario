from supabase_folder.supabase_client_manager import SupabaseClientManager

def add_class(classname: str) -> bool:
    success = False
    data = {
        "classname": classname,
        "enrollment_year": "2024"
    }
    supabase = SupabaseClientManager.get_client()

    response = None
    try:
        response = supabase.table("classes").insert(data).execute()
        if response.data:
            success = True
    except Exception as e:
        print(f"Fehler: {e}")

    return success

def delete_class(class_id: int) -> bool:
    success = False
    supabase = SupabaseClientManager.get_client()

    response = None
    try:
        response = supabase.table("classes").delete().eq("class_id", class_id).execute()
        if response.data:
            success = True
    except Exception as e:
        print(f"Fehler: {e}")

    return success

def get_all_classes_with_students_count():
    supabase = SupabaseClientManager.get_client()
    response = supabase.rpc("get_classes_with_student_count", {}).execute()

    return response.data