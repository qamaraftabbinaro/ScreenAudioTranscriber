from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper
import os
import uuid
 
app = Flask(__name__)
CORS(app)
 
# Load Whisper model
model = whisper.load_model("base")
 
@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
 
    audio_file = request.files['file']
    audio_filename = f"{uuid.uuid4()}.mp3"
    audio_file.save(audio_filename)
 
    # Transcribe audio
    result = model.transcribe(audio_filename)
    os.remove(audio_filename)  # Clean up temporary file
 
    return jsonify({"transcription": result["text"]})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
 
 