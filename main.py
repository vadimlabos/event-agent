"""
Event Agent entry point
"""
import uvicorn
from fastapi import FastAPI

from routers import status
from routers import event

app = FastAPI()
app.include_router(status.router)
app.include_router(event.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
