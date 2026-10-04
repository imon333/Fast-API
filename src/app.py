from fastapi import FastAPI
app = FastAPI()

@app.get("/moin-world")
def moin_world():
    return {"message": "Moin World!"} 