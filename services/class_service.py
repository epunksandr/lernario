from services.base_service import safe_execute_return_success, safe_execute_return_data_or_none
from supabase_folder.supabase_client_manager import SupabaseClientManager

def add_class(classname: str) -> bool:

    data = {
        "classname": classname,
        "enrollment_year": "2024"
    }
    supabase = SupabaseClientManager.get_client()

    success = safe_execute_return_success(supabase.table("classes").insert(data).execute())

    return success

def delete_class(class_id: int) -> bool:
    supabase = SupabaseClientManager.get_client()
    success = safe_execute_return_success(
        supabase.table("classes").delete().eq("class_id", class_id).execute()
    )
    return success

def get_all_classes_with_students_count():
    supabase = SupabaseClientManager.get_client()
    data = safe_execute_return_data_or_none(
        supabase.rpc("get_classes_with_student_count", {}).execute()
    )
    return data

def get_all_classnames():
    supabase = SupabaseClientManager.get_client()
    success = safe_execute_return_success(
        supabase.table("classes").select("*").execute()
    )

    return success