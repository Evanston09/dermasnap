# DermaSnap

An AI-powered mobile app that detects and analyzes acne to help users track their skin health over time.

## Project Structure

- **app/** - React Native mobile application (Expo)
- **backend/** - YOLOv8 detection API (FastAPI)

## Quick Start

### Backend

```bash
cd backend
uv sync
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
uv pip install ultralytics
uv run uvicorn main:app --host 0.0.0.0 --port 8000
```

### App

```bash
cd app
npm install
cp .env.example .env  # Configure environment variables
npm expo start
```

## Features

- Real-time acne detection using custom YOLOv8 model
- User authentication with Firebase
- Scan history tracking
- Personalized skincare insights

## Tech Stack

- **Frontend**: React Native, Expo, TypeScript
- **Backend**: FastAPI, YOLOv8, PyTorch
- **Database**: Firebase

## Disclaimer

DermaSnap is not a substitute for professional medical advice. Always consult a qualified healthcare provider for medical concerns.
