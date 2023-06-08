from fastapi import FastAPI
import redis
# import docker

# client = docker.from_env()


r = redis.Redis(host='172.18.0.2', port=6379)

app = FastAPI()

serverLoc = "loc23"

@app.get('/')
async def root():
    global serverLoc
    global r
    # return serverMsg
    return r.get(serverLoc)

