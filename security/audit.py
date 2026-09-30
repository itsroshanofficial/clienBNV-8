from database.database import execute
from database.auth import current_user

def log_action(action, entity_type=None, entity_id=None):
    user = current_user()
    if not user:
        return
    execute(
        """INSERT INTO audit_logs(company_id,user_id,action,entity_type,entity_id)
           VALUES(?,?,?,?,?)""",
        (user["company_id"], user["id"], action, entity_type, entity_id)
    )
