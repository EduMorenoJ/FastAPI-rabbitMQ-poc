from typing import List
from fastapi import FastAPI, File, UploadFile,Depends, APIRouter

router = APIRouter()

@router.post("/uploadfiles/")
async def create_upload_files(file: UploadFile = File(...)):
    return {"filenames": file.filename}