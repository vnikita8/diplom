from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shemas import *
from mock_data import *
app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_user_data/")
async def get_user_data(email:str,password:str):
    user:Student = [x for x in Students if (x.email == email) and(x.password == password) ]
    print()
    return user

@app.get("/get_groups/")
async def get_groups() -> List[Group]: 
    return Groups

@app.post("/university/create/")
async def create(item: University) -> University:
    return item

@app.patch("/university/update/")
async def update(item: University):
    return item

@app.delete("/university/delete/")
async def delete(item: University) -> University:
    return item


@app.post("/add_to_favorite_list/")
async def add_to_favorite_list(user_id:str, group_id:int) -> Student:
    user =  [x for x in Students if x.id ==user_id ][0]
    group = [x for x in Groups if x.id ==group_id ][0]
    user.favorite_list.groups.append(group)
    return user

@app.get("/get_favorite_list/")
async def get_list():
    st =Student(name="john")
    fw = FavoriteList(1,last_update="10/10/2011",student =st, comment="sds")
    return {"student":fw.student,"last_update":fw.last_update,"group": fw.groups,"comment":fw.comment}
 