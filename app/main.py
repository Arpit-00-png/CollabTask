from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def intro():
    return "hello world"