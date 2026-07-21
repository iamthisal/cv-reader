from fastapi import FastAPI , UploadFile, File
import shutil #for file handling
import os

from extractor import extract_text
from parser import parse_cv
from database import init_db, save_candidate, get_all_candidates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse



app = FastAPI()
init_db()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse ("static/index.html")


UPLOAD_DIREC = "uploaded_cvs"
os.makedirs(UPLOAD_DIREC, exist_ok=True)

@app.post("/upload")
async def upload_cv(file : UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIREC, file.filename)

    #save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)


    raw_text = extract_text(file_path)

    json_output = parse_cv(raw_text)
    save_candidate(json_output.model_dump())

    return {
        "message" : "file uploaded successfully",
        "file_path" : file_path,
        "raw data" : raw_text,
        "json data" : json_output.model_dump()
    }

@app.get("/candidates")
def list_candidate():
    return {"candidates" : get_all_candidates()}


