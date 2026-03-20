
from app.core.activity_logger import log_activity
from app.models.activity import Description
from app.db.sessions import getdb

def test_logger():
    db = next(getdb())
    
    log_activity(
        db=db,
        task_id=3,
        user_id=2,
        action_type=Description.Created,  # ← Enum member passed
        description="Test activity from test file"
    )
    
    print("✅ Logger test passed!")
    
    db.close()

if __name__ == "__main__":
    test_logger()