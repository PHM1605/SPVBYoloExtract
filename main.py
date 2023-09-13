from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import extract_detection

class ImageFolderRequest(BaseModel):
    img_dir: str # '../samples/images/'
    img_size: int # 640
    extensions: List[str] # ["*.jpg", "*.png", "*.jpeg"]
    model: str # 'rack0821.pt'

app = FastAPI()

@app.get("/extract_folder")
def get_json(img_folder: ImageFolderRequest):
    print("STARTTTT")
    response = extract_detection.extract(img_folder.model_dump())
    return response