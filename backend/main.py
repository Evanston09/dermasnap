import os
from pathlib import Path
from typing import List, Dict, Any
from contextlib import asynccontextmanager
import io

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
from ultralytics import YOLO
import numpy as np

# Global variable to store the model
model = None

# Model path configuration
MODEL_PATH = os.getenv("MODEL_PATH", "model.pt")


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    if not Path(MODEL_PATH).exists():
        print(f"Warning: Model file not found at {MODEL_PATH}")
        print("Place your custom .pt file in the project directory or set MODEL_PATH environment variable")
        model = None
    else:
        print(f"Loading YOLO model from {MODEL_PATH}...")
        model = YOLO(MODEL_PATH)
        print("Model loaded successfully!")

    yield
    model = None

# Initialize FastAPI app
app = FastAPI(
    title="YOLO Detection API",
    description="FastAPI server for object detection using YOLOv8",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "message": "YOLO Detection API is running",
        "model_loaded": model is not None,
        "model_path": MODEL_PATH
    }


@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)) -> JSONResponse:
    """
    Detect objects in an uploaded image.

    Args:
        file: Image file (jpg, jpeg, png)

    Returns:
        JSON response with detections containing bounding boxes, class labels, and confidence scores
    """
    if model is None:
        raise HTTPException(
            status_code=503,
            detail=f"Model not loaded. Please ensure your .pt file exists at {MODEL_PATH}"
        )

    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="File must be an image (jpg, jpeg, png)"
        )

    try:
        # Read image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # Convert to RGB if necessary
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Run detection
        results = model(image)

        # Parse results
        detections = []
        for result in results:
            boxes = result.boxes
            for i in range(len(boxes)):
                # Get box coordinates (xyxy format)
                box_xyxy = boxes.xyxy[i].cpu().numpy()
                x1, y1, x2, y2 = box_xyxy

                # Convert to x, y, width, height format
                x = float(x1)
                y = float(y1)
                width = float(x2 - x1)
                height = float(y2 - y1)

                # Get class and confidence
                class_id = int(boxes.cls[i].cpu().numpy())
                confidence = float(boxes.conf[i].cpu().numpy())
                class_name = model.names[class_id]

                detections.append({
                    "box": {
                        "x": x,
                        "y": y,
                        "width": width,
                        "height": height
                    },
                    "class": class_name,
                    "confidence": confidence
                })

        return JSONResponse(content={
            "detections": detections,
            "image_size": {
                "width": image.width,
                "height": image.height
            },
            "num_detections": len(detections)
        })

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing image: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
