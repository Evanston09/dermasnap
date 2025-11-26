# YOLO Detection API

A FastAPI server for object detection using YOLOv8 with custom model support.

## Features

- Upload images and get object detections with bounding boxes, class labels, and confidence scores
- Support for custom YOLOv8 models (provide your own .pt file)
- RESTful API with automatic documentation
- Model hot-reloading capability

## Setup

1. Place your custom YOLOv8 XL model file in the project directory:
   ```bash
   cp /path/to/your/model.pt .
   ```

2. Install dependencies (already done with UV):
   ```bash
   uv sync
   ```

3. Manually install ultralytics to save space and prevent CUDA dependencies
   ```bash
   uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu \
    && uv pip install ultralytics
   ```

## Running the Server

### Option 1: Using uvicorn directly
```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

### Option 2: Using the main.py script
```bash
uv run python main.py
```

### Option 3: Custom model path via environment variable
```bash
MODEL_PATH=/path/to/your/model.pt uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### 1. Health Check
```bash
curl http://localhost:8000/
```

Response:
```json
{
  "message": "YOLO Detection API is running",
  "model_loaded": true,
  "model_path": "model.pt"
}
```

### 2. Object Detection
```bash
curl -X POST "http://localhost:8000/detect" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/image.jpg"
```

Response:
```json
{
  "detections": [
    {
      "box": {
        "x": 100.5,
        "y": 200.3,
        "width": 50.2,
        "height": 75.8
      },
      "class": "person",
      "confidence": 0.95
    },
    {
      "box": {
        "x": 300.1,
        "y": 150.7,
        "width": 120.4,
        "height": 90.2
      },
      "class": "car",
      "confidence": 0.88
    }
  ],
  "image_size": {
    "width": 1920,
    "height": 1080
  },
  "num_detections": 2
}
```

### 3. Reload Model
```bash
curl -X POST "http://localhost:8000/reload-model"
```

Response:
```json
{
  "message": "Model reloaded successfully",
  "model_loaded": true
}
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Response Format

Each detection contains:
- `box`: Bounding box coordinates
  - `x`: Top-left X coordinate
  - `y`: Top-left Y coordinate
  - `width`: Box width
  - `height`: Box height
- `class`: Detected object class name
- `confidence`: Detection confidence score (0-1)

## Example Usage with Python

```python
import requests

# Upload and detect
with open("image.jpg", "rb") as f:
    response = requests.post(
        "http://localhost:8000/detect",
        files={"file": f}
    )

detections = response.json()
print(f"Found {detections['num_detections']} objects")

for det in detections['detections']:
    print(f"{det['class']}: {det['confidence']:.2f}")
```

## Configuration

- `MODEL_PATH`: Environment variable to specify custom model path (default: `model.pt`)

## Requirements

- Python 3.12+
- Custom YOLOv8 model file (.pt format)
- GPU recommended for faster inference
