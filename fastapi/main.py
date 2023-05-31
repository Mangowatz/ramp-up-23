from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8080, log_level="info")
    server = uvicorn.Server(config)
    server.run()

@app.get('/')
async def root():
    return{'example':'This is an example', 'data':999}

@app.get('/name/{yourName}')
async def getName(yourName):
    output = "Hello, "
    output += yourName
    return output
    
