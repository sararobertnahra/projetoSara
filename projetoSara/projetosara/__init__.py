import uvicorn, fastapi
def start():
    print ("Oi") 

app = fastapi.FastAPI()

@app.get("/")
def handleroot():
    return "Deu certo!"


def start():
    uvicorn.run(app,host="0.0.0.0", port=5000)