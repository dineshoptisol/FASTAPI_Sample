from typing import Optional
from fastapi import FastAPI, status, HTTPException, Response
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


# find index of the post
def find_index_of_post(id):
    for i, posts in enumerate(my_posts):
        if posts['id'] == id:
            return i

# CRUD Operations for Posts

# initial Path
@app.get("/")
def home():
    return{"message": "Welcome to FASTAPI"}

# Get all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


# Get an individual post based on id
@app.get("/post/{id}")
def get_posts(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"post with {id} does not found")
    return {"post_details": post}


# Post a single posts
@app.post("/createpost", status_code= status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,100)
    my_posts.append(post_dict)
    return {"data": post_dict}


# Update a post
@app.put("/updatepost/{id}")
def update_post(id: int, post: Post):
    index = find_index_of_post(id)
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"post with {id} does not found")
    update_post = post.model_dump()
    update_post['id'] = id
    my_posts[index] = update_post
    return {"data": update_post}


# Delete a single post
@app.delete("/deletepost/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_of_post(id)
    if index == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail = f"post with {id} does not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)