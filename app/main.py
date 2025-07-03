"""main.py."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/proxy")
async def controller(request: Request):
    return JSONResponse(
        content={
            "body": await request.body(),
            "headers": request.headers,
            "method": request.method,
        },
        status_code=200,
        headers=request.headers,
    )


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
    }
