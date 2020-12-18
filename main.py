from fastapi import FastAPI
from datetime import datetime
import platform

app = FastAPI()


@app.get("/")
async def root():

    return {"message": "Hello World",
            "datetime": datetime.now(),
            "system": platform.version()
            }
