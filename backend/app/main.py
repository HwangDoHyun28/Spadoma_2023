from fastapi import FastAPI, File, UploadFile
from tempfile import NamedTemporaryFile
from typing import IO
from starlette.middleware.cors import CORSMiddleware

import pandas as pd
import openpyxl
import json

from fastapi import Depends, HTTPException, status
from sqlmodel import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 


app = FastAPI()

origins = [
    "http://127.0.0.1:5173",    # 또는 "http://localhost:5173" "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def get_session() -> Session:
    # engine은 각자 Db환경에 따라 달라지므로 생략
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    with session() as session:
        yield session

@app.post("/upload_file")
def upload_file(
    file: UploadFile = File(...), 
    db: Session = Depends(get_session)
    ) -> None:
    # formdat로 업로드한 파일을 읽는다.
    read_file = file.read()
    
    # pandas 모듈을 사용하여 업로드한 파일을 pandas.Dataframe 형식으로 가져온다.
    excel_file = pd.read_excel(read_file)
    
    # Dataframe 인스턴스를 json 으로 각 row마다 나누어 리스트화 시킨다.
    json_data = excel_file.to_json(orient='records')
    
    # raw한 json데이터를 읽는다.
    data = json.loads(json_data)
    
    # 각 row 데이터에 해당하는 json을 테이블에 매핑 후 bulk_create한다.
    for row in data:
        model = TableModel(**row)
        db.add(model)
        
    db.commit()
    return









