from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shemas import *
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

@app.post("/university/create/")
async def create(item: University):
    return item

@app.patch("/university/update/")
async def update(item: University):
    return item

@app.delete("/university/delete/")
async def delete(item: University):
    return item


@app.post("/add_to_favorite_list/")
async def add_to_favorite_list(item:Group):
    st =Student(name="john")
    fw = FavoriteList(1,last_update="10/10/2011",student =st, comment="sds")
    fw.groups.append(item)
    print()
    return {"student":fw.student,"last_update":fw.last_update,"group": fw.groups,"comment":fw.comment}

@app.get("/get_favorite_list/")
async def get_list():
    st =Student(name="john")
    fw = FavoriteList(1,last_update="10/10/2011",student =st, comment="sds")
    return {"student":fw.student,"last_update":fw.last_update,"group": fw.groups,"comment":fw.comment}
