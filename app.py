from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}
