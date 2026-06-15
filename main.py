from fastapi import FastAPI , UploadFile, File
import shutil #for file handling
import os

app = FastAPI()

UPLOAD_DIREC = "uploaded_cvs"
os.makedirs(UPLOAD_DIREC, exist_ok=True)

@app.post("/upload")
async def upload_cv(file : UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIREC, file.filename)

    #save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    return {
        "message" : "file uploaded successfully",
        "file_path" : file_path
    }
