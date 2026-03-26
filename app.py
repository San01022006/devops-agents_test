from fastapi import FastAPI

app = FastAPI()

def add(a, b):
    return a + b

@app.get("/")
def home():
    return {"message": "DevOps Pipeline Working!"}
