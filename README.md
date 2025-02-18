# ScreenAudioTranscriber


# Screen Audio Transcriber

## Overview
Screen Audio Transcriber is a web-based application that records system audio during screen sharing and sends recorded audio clips to a backend server for processing/transcription. The application is built using vanilla JavaScript and Bootstrap for the user interface.

## Key Features
- Screen sharing with system audio capture
- Audio recording in 3-second intervals
- Automatic upload to backend server
- Audio playback functionality
- Bootstrap-based responsive UI

## Prerequisites
- A modern browser supporting the **MediaRecorder API** (Chrome/Firefox/Edge)
- Backend server endpoint for handling audio uploads
- HTTPS connection (required for screen sharing)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ScreenAudioTranscriber.git
   ```
2. No dependencies required (all libraries are CDN-based).
3. Open `index.html` in a browser.

## Usage
1. Click **"Start Screen Share"** (enable system audio sharing in the browser prompt).
2. Click **"Start Recording"** to begin capturing audio.
3. The system automatically:
   - Records 3-second audio chunks.
   - Sends them to the backend server.
   - Continues recording until stopped.
4. Click **"Stop Recording"** to end the session.
5. Playback recorded audio using the built-in player.

## Technical Details
### Key Components
- **Media Stream Handling:** Uses `getDisplayMedia()` for screen + audio capture.
- **Audio Recording:** Utilizes the `MediaRecorder` API with WebM/Opus format.
- **Chunk Processing:**
  - Records in 3-second intervals.
  - Automatically uploads via `fetch()`.
  - Displays results in the UI.

### Code Structure
```
- index.html
  - Bootstrap UI components
  - Recording controls
  - Status display
  - Audio player
- Script Section
  - Media stream management
  - Recording lifecycle handlers
  - Automatic upload implementation
  - 3-second interval logic
```

### Audio Format
- **Format:** WebM
- **Codec:** Opus
- **Chunk Size:** 3 seconds

## Backend Integration
Configure your .NET Core endpoint in the `sendAudioToServer` function:
```javascript
await fetch('http://your-backend/transcribe', {
  method: 'POST',
  body: formData
});
```
> **Note:** Update the IP/port in the provided code (`103.192.152.69:5000`) to match your server details.

## Limitations
- Requires user interaction to start recording.
- Browser-specific audio capture implementation.
- Dependent on backend server availability.
- No error handling for failed uploads.

## Potential Improvements
- Add WebSocket support for real-time transcription.
- Implement retry logic for failed uploads.
- Add format conversion options (MP3/WAV).
- Include visual feedback for recording status.
- Add authentication layer for API calls.

