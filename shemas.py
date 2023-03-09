from typing import Union, List
from enum import Enum
from fastapi import FastAPI
from dataclasses import dataclass
from datetime import date
from pydantic import BaseModel
class Education_level(Enum):
    Специалитет = 1
    Бакалавриат = 2
    Магистратура =3
    
@dataclass
class Place(BaseModel):
    id:int
    speciality: object
    education_level: int
    education_program:str
    fed_budget_seats:int
    regional_budget_seats:int
    non_budget_seats:int

@dataclass
class University(BaseModel):
    id:int
    name: str
    description: Union[str, None] = None
    list_places: Union[List[Place],None] = None
    university_staff: Union[list, None] = None


class Student(BaseModel):
    name:str

class Group(BaseModel):
    id:int
    name: str
    year_of_recruitment:int
    available_places:int
    potential_places:int
    course:int
    end_year:int
    
    
class FavoriteList():
    id:int
    last_update:date
    student:Student
    groups: list[Group] = []
    comment:str
    __priority__:int
    
    def __init__(self,id,student,last_update,comment):
        self.id, self.student,self.last_update, self.comment= id,student,last_update,comment
    
    
    
