from fastapi import FastAPI , UploadFile, File
import shutil #for file handling
import os

from extractor import extract_text
from parser import parse_cv



app = FastAPI()

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

    return {
        "message" : "file uploaded successfully",
        "file_path" : file_path,
        "raw data" : raw_text,
        "json data" : json_output
    }
