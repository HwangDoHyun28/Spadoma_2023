from fastapi import FastAPI
from app.celery_worker import divide
from datetime import datetime

from db.database import db_context

from db.models import Base, Task
from db.database import engine
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/result")
async def get_task(task_id: str):
    with db_context() as s:
        t = s.query(Task).filter(Task.task_id == task_id).first()
    return t

@app.get("/divide")
async def run_divide(input_a: int, input_b: int):
    job = divide.apply_async([input_a, input_b])
    with db_context() as s:
        t = Task(status="running", start_date=datetime.now(), task_id=job.id)
        s.add(t)
        s.commit()
        s.refresh(t)
    return t
