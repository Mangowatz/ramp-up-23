from fastapi import FastAPI
import redis

r = redis.Redis(host='172.18.0.2', port=6379)#ip on redis container

app = FastAPI()

serverMsg = "No Previous Value"
serverLoc = "loc23"
r.set(serverLoc,serverMsg)

def getMsg():
    global serverLoc
    global r
    # return serverMsg
    return r.get(serverLoc)

def setMsg(msg:str):
    global serverLoc
    global r
    # serverMsg = msg
    return r.set(serverLoc,msg)

@app.get('/')
async def root():
    return getMsg()

@app.post('/{msg}')
async def post(msg:str):
    setMsg(msg)
    return getMsg()