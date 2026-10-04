from fastapi import FastAPI, HTTPException

from src.schemas import PostCreate

app = FastAPI()

text_posts = {
    1: {
        "title": "Getting Started with FastAPI",
        "content": "FastAPI makes building high-performance Python REST APIs quick and intuitive."
    },
    2: {
        "title": "Why Virtual Environments Matter",
        "content": "Isolated environments prevent package dependency conflicts across your projects."
    },
    3: {
        "title": "Understanding HTTP Methods",
        "content": "GET retrieves data, POST submits data, and PUT updates existing resources."
    },
    4: {
        "title": "Mastering Git Basics",
        "content": "Commit early and push often to keep track of your code history safely."
    },
    5: {
        "title": "Introduction to Pydantic",
        "content": "Pydantic ensures data validation and settings management using standard Python types."
    },
    6: {
        "title": "Asynchronous Python Explained",
        "content": "Asyncio allows Python programs to handle multiple task executions concurrently."
    },
    7: {
        "title": "Building RESTful APIs",
        "content": "Design clear endpoints with standard status codes to build intuitive web APIs."
    },
    8: {
        "title": "Database Indexing Tips",
        "content": "Indexes speed up query read operations but add slight overhead to database writes."
    },
    9: {
        "title": "Writing Clean Code",
        "content": "Clear variable naming and short functions make your codebase easy to maintain."
    },
    10: {
        "title": "Deploying Python Apps",
        "content": "Containerize your app with Docker for seamless and consistent cloud deployments."
    }
}

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts[id]
    
    
# post endpoint

@app.post("/posts")
def create_post(post: PostCreate) -> PostCreate:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post


