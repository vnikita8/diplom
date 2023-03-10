from typing import Union, List
from uuid import uuid4
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
    

class Group(BaseModel):
    id:int
    name: str
    year_of_recruitment:int
    available_places:int
    potential_places:int
    course:int
    end_year:int
    
    def create(id,name,year_of_recruitment,available_places,potential_places,course,end_year):
        
        return(Group(id = id,name=name,year_of_recruitment=year_of_recruitment,
                     available_places = available_places,potential_places=potential_places,
                     course=course,end_year=end_year))
    
class FavoriteList(BaseModel):
    last_update:Union[str, None] = None
    groups: list[Group] = []
    comment:Union[str, None] = None
    
    def create(self,last_update):
        self.last_update = last_update
    
class Student(BaseModel):
    id:str
    first_name:str
    middle_name:str
    last_name:str
    phone:str = "8-800-555-35-35"
    email:str = "default@mail.com"
    contact_email:str ="fault@mail.com" 
    password:str
    favorite_list: FavoriteList = FavoriteList(last_update=date.today().strftime('%Y-%m-%d'),comment="dddd")
    
    def create(first_name,middle_name,last_name):
        return Student(id = "ц",first_name=first_name,middle_name=middle_name,last_name=last_name, password="None")

    
class StudentShema(BaseModel):
    id:str 
    first_name:str
    middle_name:str
    last_name:str
    phone:str = "8-800-555-35-35"
    email:str = "default@mail.com"
    contact_email:str ="fault@mail.com" 
    password:str