from fastapi import FastAPI
import uvicorn

from app.routes import router


app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Conversation Proxy Service!"}


def start():
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
