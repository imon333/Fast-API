from fastapi import FastAPI, HTTPException
app = FastAPI()

text_posts = {1: {"title": "First Post", "content": "This is the first post."},
              2: {"title": "Second Post", "content": "This is the second post."}}

@app.get("/posts")
def get_all_posts():
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return text_posts[id]
    