from http.client import HTTPException
from sqlite3 import Date
from typing import Type
from sqlalchemy.orm import Session
from sqlalchemy import func, desc, asc, update
from sqlalchemy.sql import text
from sqlalchemy.dialects import postgresql
from schemas import operation, substance, user
from datetime import date, datetime
import models


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# запрос пользователя по логину
def get_user_by_login(db: Session, user: user.UserCheck,):
    db_user = db.query(models.User).filter(models.User.login == user.username, models.User.password == user.password).first()
    return db_user 


def get_users(db: Session):
    return db.query(models.User).all()


def get_users_count(db: Session):
    return db.query(models.User).count()

def get_amount(db: Session, list, skip: int, limit: int):
    if list is not None:
        if list[0] == "id":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.id.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.id.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "name":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.name.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.name.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "units":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.units.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.units.desc()).offset(skip).limit(limit).all() 
       
        if list[0] == "amount":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.amount.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).order_by(models.Stock_Amount.amount.desc()).offset(skip).limit(limit).all() 
    return db.query(models.Stock_Amount).offset(skip).limit(limit).all()

def get_amount_by_substance(db: Session, substance: str, list, skip: int, limit: int):
    if list is not None:
        if list[0] == "id":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.id.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.id.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "name":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.name.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.name.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "units":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.units.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.units.desc()).offset(skip).limit(limit).all() 
       
        if list[0] == "amount":
            if list[1] == "ASC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.amount.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).order_by(models.Stock_Amount.amount.desc()).offset(skip).limit(limit).all() 
    return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).offset(skip).limit(limit).all()


def get_amount_substance(substance: str, db: Session):
    return db.query(models.Stock_Amount).filter(models.Stock_Amount.name == substance).first()

def get_substance_id(substance: str, db: Session):
    return db.query(models.Substance).filter(models.Substance.name == substance).first()

def get_operations(db: Session, list: list, skip: int, limit: int):
    if list is not None:
        if list[0] == "id":
            if list[1] == "ASC":
                return db.query(models.Operation).order_by(models.Operation.id.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).order_by(models.Operation.id.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
        
        if list[0] == "substance.name":
            if list[1] == "ASC":
                return db.query(models.Operation).join(models.Substance).join(models.User).join(models.Operation_Type).order_by(models.Substance.name.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).join(models.Substance).join(models.User).join(models.Operation_Type).order_by(models.Substance.name.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "amount":
            if list[1] == "ASC":
                return db.query(models.Operation).order_by(models.Operation.amount.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).order_by(models.Operation.amount.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
       
        if list[0] == "user.surname":
            if list[1] == "ASC":
                return db.query(models.Operation).order_by(models.User.surname.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).order_by(models.User.surname.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
        
        if list[0] == "date":
            if list[1] == "ASC":
                return db.query(models.Operation).order_by(models.Operation.date.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).order_by(models.Operation.date.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 

    return db.query(models.Operation).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all()

def get_operations_by_substance(db: Session, substance: str, list: list, skip: int, limit: int):
    substance_id = get_substance_id(substance, db)
    if substance_id is None:
        return 
    if list is not None:
        if list[0] == "id":
            if list[1] == "ASC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.Operation.id.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all()                
            if list[1] == "DESC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.Operation.id.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
        
        if list[0] == "substance.name":
            if list[1] == "ASC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).join(models.Substance).join(models.User).join(models.Operation_Type).order_by(models.Substance.name.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).join(models.Substance).join(models.User).join(models.Operation_Type).order_by(models.Substance.name.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "amount":
            if list[1] == "ASC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.Operation.amount.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.Operation.amount.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
       
        if list[0] == "user.surname":
            if list[1] == "ASC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.User.surname.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.User.surname.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
        
        if list[0] == "date":
            if list[1] == "ASC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.Operation.date.asc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).order_by(models.Operation.date.desc()).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all() 

    return db.query(models.Operation).filter(models.Operation.fk_substance_id == substance_id.id).join(models.Substance).join(models.User).join(models.Operation_Type).offset(skip).limit(limit).all()


def get_operations_types(db: Session):
    return db.query(models.Operation_Type).all()


def get_substances(db: Session, list: list, skip: int, limit: int):
    
    if list is not None:
        if list[0] == "id":
            if list[1] == "ASC":
                return db.query(models.Substance).order_by(models.Substance.id.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).order_by(models.Substance.id.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "name":
            if list[1] == "ASC":
                return db.query(models.Substance).order_by(models.Substance.name.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).order_by(models.Substance.name.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "element_number":
            if list[1] == "ASC":
                return db.query(models.Substance).order_by(models.Substance.element_number.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).order_by(models.Substance.element_number.desc()).offset(skip).limit(limit).all() 
       
        if list[0] == "type":
            if list[1] == "ASC":
                return db.query(models.Substance).order_by(models.Substance.type.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).order_by(models.Substance.type.desc()).offset(skip).limit(limit).all() 
        
    return db.query(models.Substance).offset(skip).limit(limit).all()

def get_substances_by_name(db: Session, substance: str, list: list, skip: int, limit: int):
    if list is not None:
        if list[0] == "id":
            if list[1] == "ASC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.id.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.id.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "name":
            if list[1] == "ASC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.name.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.name.desc()).offset(skip).limit(limit).all() 
        
        if list[0] == "element_number":
            if list[1] == "ASC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.element_number.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.element_number.desc()).offset(skip).limit(limit).all() 
       
        if list[0] == "type":
            if list[1] == "ASC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.type.asc()).offset(skip).limit(limit).all() 
            if list[1] == "DESC":
                return db.query(models.Substance).filter(models.Substance.name==substance).order_by(models.Substance.type.desc()).offset(skip).limit(limit).all() 
        
    return db.query(models.Substance).offset(skip).limit(limit).all()

def get_operations_count(db: Session):
    return db.query(models.Operation).count()

def get_stocks_count(db: Session):
    return db.query(models.Stock_Amount).count()

def get_operation(db: Session, id: int):
    return db.query(models.Operation).filter(models.Operation.id == id).first()

def get_substance(db: Session, id: int):
    return db.query(models.Substance).filter(models.Substance.id == id).first()

def get_substances_count(db: Session):
    return db.query(models.Substance).count()

def get_substances_names(db: Session):
    return db.query(models.Substance.id, models.Substance.name).all()

def add_operation(db:Session, operation: operation.OperationCreate):
    user = (operation.dict().get('user')).split()
    userName = user[0]
    userSurname = user[1]
    Operation_Type = operation.dict().get('type')
    Substance = operation.dict().get('substance')
    Amount = operation.dict().get('amount')
    if Operation_Type == 'Remove' and Amount > 0:
        Amount = -Amount
    date = operation.dict().get('date')
    user = db.query(models.User.id).filter(models.User.surname == userSurname, models.User.name == userName).first()
    type = db.query(models.Operation_Type.id).filter(models.Operation_Type.type == Operation_Type).first()
    substance = db.query(models.Substance.id).filter(models.Substance.name == Substance).first()
    db_operation = models.Operation(fk_substance_id = substance.id,  fk_operation_type_id = type.id, fk_user_id = user.id, date = date, amount = Amount)
    db.add(db_operation)
    db.commit()
    db.refresh(db_operation)
    return  db_operation

def delete_operation(db: Session, id: int):
    operation = db.query(models.Operation).filter(models.Operation.id == id).first()
    if not operation:
        raise HTTPException(status_code=404, detail="Operation not found")
    db.delete(operation)
    db.commit()
    return {"ok": True}

def delete_substance(db: Session, id: int):
    substance = db.query(models.Substance).filter(models.Substance.id == id).first()
    if not operation:
        raise HTTPException(status_code=404, detail="Substance not found")
    db.delete(substance)
    db.commit()
    return {"ok": True}
    
def add_substance(db:Session, substance: substance.SubstanceCreate):
    db_substance = models.Substance(element_number=substance.element_number, name=substance.name, cas=substance.cas, formula=substance.formula, units=substance.units, type=substance.type)
    db.add(db_substance)
    db.commit()
    db.refresh(db_substance)
    return db_substance

def update_operation(db: Session, id:int, operation: operation.Operation):
    user = operation.dict().get('user')
    Operation_Type = operation.dict().get('type')
    Substance = operation.dict().get('substance')
    Amount = operation.dict().get('amount')
    if Operation_Type.get('type') == 'Remove' and Amount > 0:
        Amount = - Amount
    date = operation.dict().get('date')  
    db_operation = get_operation(db, id)
    user = db.query(models.User.id).filter(models.User.surname == user.get('surname')).one()
    type = db.query(models.Operation_Type.id).filter(models.Operation_Type.type == Operation_Type.get('type')).one()
    substance = db.query(models.Substance.id).filter(models.Substance.name == Substance.get('name')).one()
    db_operation.fk_substance_id = substance.id
    db_operation.fk_operation_type_id = type.id
    db_operation.fk_user_id = user.id
    db_operation.date = date
    db_operation.amount = Amount
    db.commit()
    db.refresh(db_operation)
    return db_operation

def update_substance(db: Session, id:int, substance: substance.SubstanceShow):
    db_substance = get_substance(db, id)
    db_substance.name = substance.dict().get('name')
    db_substance.element_number = substance.dict().get('element_number') 
    db_substance.cas = substance.dict().get('cas') 
    db_substance.units = substance.dict().get('units')
    db_substance.cas = substance.dict().get('cas') 
    db_substance.type = substance.dict().get('type')
    db.commit()
    db.refresh(db_substance)
    return db_substance