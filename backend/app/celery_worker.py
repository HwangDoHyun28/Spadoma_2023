from app.celery_app import celery_task
from db.database import db_context
from db.models import Task
from datetime import datetime

@celery_task.task
def divide(x, y):
    import time
    time.sleep(10)
    result = x / y

    with db_context() as s:
        task = s.query(Task).filter(Task.task_id == divide.request.id).first()
        task.status = "finished"
        task.result = str(result)
        task.end_date = datetime.now()
        s.commit()

    return result
