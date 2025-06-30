from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
from obstacle_detector import detect_obstacles

app = FastAPI()


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        # Save uploaded image
        os.makedirs("images", exist_ok=True)
        file_path = f"images/{file.filename}"
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        # Run detection
        result = detect_obstacles(file_path)

        # Clean up
        os.remove(file_path)

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
