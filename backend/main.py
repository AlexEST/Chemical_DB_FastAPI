from datetime import datetime, timedelta
from dataclasses import field
from typing import List, Union
import json
from fastapi import Depends, FastAPI, HTTPException, Response, Request
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI
import models, crud
from schemas import operation, operationType, substance, user
from database import SessionLocal, engine

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.responses import Response
from starlette.status import HTTP_200_OK



models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# uvicorn main:app --reload
app = FastAPI()




origins = [
    "http://localhost:3000",
    "http://localhost",
    "http://localhost:8080",
    ]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post("/token")
async def login(response: Response, user: user.UserCheck, db: Session = Depends(get_db)):
    User = crud.get_user_by_login(db, user)
    if not User:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(1)

    return {"username": user.username , "fullName": {User.name +' '+ User.surname}}

@app.get("/users/", response_model=List[user.UserShow])
def read_users(response: Response, db: Session = Depends(get_db)):
    users = crud.get_users(db)
    usersLen = str(len(users))
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = usersLen
    return users



@app.get("/stock/")
def get_Stock(request: Request,  response: Response, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orderList = request.query_params.get('sort')
    rangeList = request.query_params.get('range')
    if orderList is not None:
        orderList = json.loads(request.query_params.get('sort')) 
    else:
        orderList = ["id","ASC"]
    if rangeList is not None:
        rangeList = json.loads(request.query_params.get('range')) 
        skip = rangeList[0]
        limit = (rangeList[1]+1) - skip
    stock = crud.get_amount(db, orderList, skip=skip, limit=limit)
    stockLen = crud.get_stocks_count(db)
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(stockLen)
    return stock

@app.get("/stock/substance")
def get_Substance_Stock(request: Request, response: Response, db: Session = Depends(get_db)):
    req = json.loads(request.query_params.get('filter')) 
    substance = str(req.get('name'))
    sub_stock = crud.get_amount_substance(substance, db)
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(1)
    return sub_stock

@app.get("/operations/", response_model=List[operation.Operation])
def get_Operations(response: Response, request: Request, skip: int = 0, limit: int = 100,   db: Session = Depends(get_db)):
    orderList = request.query_params.get('sort')
    rangeList = request.query_params.get('range')
    filterList = request.query_params.get('filter')
    if filterList is not None:
        filterList = json.loads(request.query_params.get('filter'))
        filt = filterList.get('name')       
    if orderList is not None:
        orderList = json.loads(request.query_params.get('sort')) 
    else:
        orderList = ["id","ASC"]
    if rangeList is not None:
        rangeList = json.loads(request.query_params.get('range')) 
        skip = rangeList[0]
        limit = (rangeList[1]+1) - skip
    if filterList is not None and filt is not None:
        filt = str(filt).capitalize()
        operations = crud.get_operations_by_substance(db, substance=filt, list=orderList, skip=skip, limit=limit)
        if operations is None:
            operations = crud.get_operations(db, orderList, skip=skip, limit=limit)
    else:
        operations = crud.get_operations(db, orderList, skip=skip, limit=limit)
    operLen = crud.get_operations_count(db)
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(operLen)
    return operations

@app.get("/operationsTypes/",  response_model=List[operationType.Operation_Type])
def get_Operations_Types(db: Session = Depends(get_db)):
    types = crud.get_operations_types(db)
    return types

@app.get("/substances/",  response_model=List[substance.SubstanceShow])
def get_substances(response: Response, request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rangeList = request.query_params.get('range') 
    orderList = request.query_params.get('sort')
    filterList = request.query_params.get('filter')
    if filterList is not None:
        filterList = json.loads(request.query_params.get('filter'))
        filt = filterList.get('name')
        
    if orderList is not None:
        orderList = json.loads(request.query_params.get('sort')) 
    else:
        orderList = ["id","ASC"]
    if rangeList is not None:
        rangeList = json.loads(request.query_params.get('range')) 
        skip = rangeList[0]
        limit = (rangeList[1]+1) - skip   
    if filterList is not None and filt is not None:
        subfilt = str(filt).capitalize()
        substances = crud.get_substances_by_name(db, substance=subfilt, list=orderList, skip=skip, limit=limit)
        if substances is None:
            substances = crud.get_substances(db, list=orderList, skip=skip, limit=limit)  
    else:
        substances = crud.get_substances(db, list=orderList, skip=skip, limit=limit)
    subLen = crud.get_substances_count(db)
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(subLen) 
    return substances

@app.get("/operations/{id}", )
def get_operation(response: Response, id: int, db: Session = Depends(get_db)): 
    operation = crud.get_operation(db, id)
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(1)
    return operation


@app.get("/substances/{id}", )
def get_substance(response: Response, id: int, db: Session = Depends(get_db)): 
    substance = crud.get_substance(db, id)
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(1)
    return substance

@app.get("/substancesNames/")
def get_substances_names(response: Response, db: Session = Depends(get_db)):
    substancesNames = crud.get_substances_names(db)
    namesLen = str(len(substancesNames))
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = namesLen

    return substancesNames

@app.post("/add/operations", response_model=operation.Operation)
def add_Operations(operation: operation.OperationCreate, db: Session = Depends(get_db)):
    add_Operation = crud.add_operation(db, operation)
    return add_Operation

@app.post("/add/substances", response_model=substance.SubstanceShow)
def add_Substances(substance: substance.SubstanceCreate, db: Session = Depends(get_db)):
    add_Substance = crud.add_substance(db, substance)
    return add_Substance

@app.delete("/operations/{id}")
def delete_Operation(id: int, db: Session = Depends(get_db)):
    return crud.delete_operation(db, id)

@app.delete("/substances/{id}")
def delete_Substance(id: int, db: Session = Depends(get_db)):
    return crud.delete_substance(db, id)

@app.put("/operations/{id}", response_model=operation.Operation)
def update_Operation(response: Response, operation: operation.Operation, id: int, db: Session = Depends(get_db)):
    response.headers['Access-Control-Expose-Headers'] = 'X-Total-Count'
    response.headers['X-Total-Count'] = str(1)
    return crud.update_operation(db, id, operation)

@app.put("/substances/{id}", response_model=substance.SubstanceShow)
def update_Substance(substance: substance.SubstanceShow, id: int, db: Session = Depends(get_db)):
    return crud.update_substance(db, id, substance) 

