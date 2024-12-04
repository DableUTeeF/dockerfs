from fastapi import FastAPI, File, UploadFile, status, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()


@app.get('/')
def _file_upload(file: UploadFile, text: str):
    
    return HTMLResponse('hello world')
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, log_level="debug")
