"""main.py."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/proxy")
async def controller(request: Request):
    content = await request.json()
    headers: dict = {}
    for k, v in request.headers.items():
        headers[k] = v
    return JSONResponse(
        content={
            "body": content,
            "headers": headers,
            "method": request.method,
        },
        status_code=200,
    )


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
    }
