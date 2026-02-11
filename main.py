from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return {"message": "API is running"}


@app.get('/blog')
def index(limit, published : bool ,sort: Optional[str] = None):
    if published:
     return {"data": f"{limit} blogs from the db"}
    else:
        return{'data':f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {"data": "all unpublished blogs"}

@app.get('/blog/{id}')
def show(id: int):
    return {"data": id}

@app.get('/blog/{id}/comments')
def comments(id: int):
    return {
        "data": ["comment1", "comment2"]
    }

class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return{
        'data':f"blog is Created with title as my {blog.title}"
    }

#if __name__ == "__main__":
   # uvicorn.run(app,host = "127.0.0.1",port = 9000)
