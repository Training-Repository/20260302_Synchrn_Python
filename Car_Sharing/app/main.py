from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Depends
from .schemas import Car, CarInput
from .schemas import Car_DBModel

from contextlib import asynccontextmanager

from sqlmodel import create_engine
from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import select

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False},  

    echo=True
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    SQLModel.metadata.create_all(engine) 

    # App execution
    yield

    # Shutdown code
    print("That's all folks!")
    
app = FastAPI(title="Car API", lifespan=lifespan)

def get_session():
    with Session(engine) as session:
        yield session

data = [
    {"id": 1, "size": "s", "fuel": "petrol",    "doors": 3, "transmission": "auto"},
    {"id": 2, "size": "s", "fuel": "electric",  "doors": 3, "transmission": "auto"},
    {"id": 3, "size": "s", "fuel": "petrol",    "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric",  "doors": 3, "transmission": "auto"},
    {"id": 5, "size": "m", "fuel": "hybrid",    "doors": 5, "transmission": "auto"},
    {"id": 6, "size": "m", "fuel": "petrol",    "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "diesel",    "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "l", "fuel": "electric",  "doors": 5, "transmission": "auto"},
    {"id": 9, "size": "l", "fuel": "hybrid",    "doors": 5, "transmission": "auto"}
]


def load_data(data):
    return [Car.model_validate(obj) for obj in data]

db = load_data(data)




@app.post("/api/cars/migrate")
def migrate_data_to_db() -> list[Car_DBModel]:
    '''Currently, will duplicate if called multiple times.
    Trips data is not migrated as no data model for trips created yet.'''
    with Session(engine) as session:
        for car in db:
            new_car = Car_DBModel.model_validate(car)
            session.add(new_car)
        session.commit()
    return db

@app.get("/")
async def welcome(name = ''):                        # http://localhost:8000/?name=Ramakant
    """Returns a friendly welcome message"""
    return {"message": f"Welcome {name}, to the Car Sharing service!"}

@app.get("/api/cars")
def get_cars(size:str|None=None, doors:int|None=None, session: Session = Depends(get_session))->list[Car]:
    query = select(Car_DBModel)
    if size is not None:
        query = query.where(Car_DBModel.size == size)
    if doors is not None:
        query = query.where(Car_DBModel.doors >= doors)
    
    result = session.exec(query).all()
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f"No cars with size={size} and doors>={doors}.")

@app.get("/api/cars/{id}")
def car_by_id(id:int, session: Session = Depends(get_session))->Car_DBModel:
    car = session.get(Car_DBModel, id)
    if car:
        print(type(car))
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id = {id}.")

@app.post("/api/cars/", response_model=Car_DBModel)
def add_car(car: CarInput, session: Session = Depends(get_session)) -> Car_DBModel:
    new_car = Car_DBModel.model_validate(car)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car

@app.delete("/api/cars/{id}", status_code=204)
def remove_car(id: int, session: Session = Depends(get_session)) -> None:
    car = session.get(Car_DBModel, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")
    
@app.put("/api/cars/{id}", response_model=Car_DBModel)
def change_car(id: int, new_data: CarInput, session: Session = Depends(get_session)) -> Car_DBModel:
    car = session.get(Car_DBModel, id)
    if car:
        car.fuel = new_data.fuel
        car.size = new_data.size
        car.doors = new_data.doors
        car.transmission = new_data.transmission

        session.commit()
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")