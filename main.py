from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Hello TutLinks.com"}
@app.get("/app")
def home():
    return {"message":"Hello TutLinks.com"}
