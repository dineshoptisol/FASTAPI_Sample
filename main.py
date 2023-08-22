from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

# Global variable to store posts locally
my_posts = [{"title": "FAST API 1", "content": "This is my first time building an API 1", "id": 1},
            {"title": "FAST API 2", "content": "This is my first time building an API 2", "id": 2} ]

# Base model for Posts
# This BaseModel always returns as Dictonary
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# Find individual post
def find_post(id):
    for posts in my_posts:
        if posts["id"] == id:
            return posts

# CRUD Operations for Posts
# Get all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}

# Get an individual post based on id
@app.get("/posts/{id}")
def get_posts(id: int):
    post = find_post(id)
    return {"post_details": post}
    

# Post a single posts
@app.post("/posts")
def create_post(post: Post):
   post_dict = post.model_dump()
   post_dict['id'] = randrange(0,100)
   my_posts.append(post_dict)
   return {"data": post_dict}

