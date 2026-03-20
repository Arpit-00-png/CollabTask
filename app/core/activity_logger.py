from sqlmodel import Session 
from app.models.activity import Description,Activity

def log_activity(db : Session , task_id: int , user_id: int, action_type: Description, description : str):

    newactivity = Activity(action_type=action_type,description=description, task_id=task_id, user_id=user_id)
    db.add(newactivity)
    return 