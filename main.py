from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from obstacle_detector import detect_obstacles
import shutil
import os

app = FastAPI()


# ----------- YOLO OBSTACLE DETECTION -----------
@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    os.makedirs("images", exist_ok=True)
    file_location = f"images/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = detect_obstacles(file_location)
    os.remove(file_location)

    return JSONResponse(content=result)
