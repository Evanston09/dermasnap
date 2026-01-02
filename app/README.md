# DermaSnap

A React Native mobile application that uses AI to detect and analyze acne, helping users track their skin health over time.

## Overview

DermaSnap allows users to take photos of their face to detect acne spots using machine learning. The app provides personalized insights, tracks scan history, and offers skincare tips to help manage acne conditions.

## Technologies

- **React Native** with **Expo** - Cross-platform mobile development
- **TypeScript** - Type-safe JavaScript
- **Firebase** - User authentication
- **AsyncStorage** - Local data persistence
- **Expo Camera & Image Picker** - Photo capture and gallery access

## Environment Variables

Create a `.env` file in the app directory (see `.env.example`):

```env
EXPO_PUBLIC_CSAI_BASE_URL=http://localhost:8000

# Firebase Configuration
EXPO_PUBLIC_FIREBASE_API_KEY=your_api_key_here
EXPO_PUBLIC_FIREBASE_AUTH_DOMAIN=your_auth_domain_here
EXPO_PUBLIC_FIREBASE_PROJECT_ID=your_project_id_here
EXPO_PUBLIC_FIREBASE_STORAGE_BUCKET=your_storage_bucket_here
EXPO_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_sender_id_here
EXPO_PUBLIC_FIREBASE_APP_ID=your_app_id_here
EXPO_PUBLIC_FIREBASE_MEASUREMENT_ID=your_measurement_id_here
```

## Setup

1. Install dependencies:
```bash
npm install
```

2. Copy and configure environment variables:
```bash
cp .env.example .env
```

3. Update `.env` with your Firebase credentials and backend URL

4. Start the development server:
```bash
npm expo start
```

5. Run on your platform:
```bash
npm run ios      # iOS
npm run android  # Android
npm run web      # Web
```

## Disclaimer

DermaSnap is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.
