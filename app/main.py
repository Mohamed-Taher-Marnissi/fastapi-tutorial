from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# with can remove this command and use alembic migration tool
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()       

# origins = ["https://www.google.com/"] accessible by google only
origins = ["*"]  # public Accessible by everyone

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

# def create_posts(payLoad: dict = Body(...)):
# convert the pydantic model to a dict post.dict()
# cursor_factory = RealDictCursor   => By using RealDictCursor, each row fetched from the database will be represented as 
# a dictionary where the keys are the column names and the values are the corresponding column values.    

# def find_index_post(id):
#     for i , p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message" : "Hello World"}



