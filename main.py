from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my api"}

@app.get("/posts")
def get_users():
    return {"data": "All users are here"}

@app.post("/createpost")
def create_post(payload: dict = Body()):
    print(payload)
    return {"new_post": f"title: {payload['title']} content: {payload['content']}"}