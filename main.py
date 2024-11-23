from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse, HTMLResponse
import cv2
import face_recognition
import numpy as np
from pathlib import Path
import shutil

# Initialize FastAPI app
app = FastAPI()

# Folder paths
TRAINING_IMAGES_PATH = Path("training_images")
TRAINING_IMAGES_PATH.mkdir(exist_ok=True)

# Known face encodings and names
known_encodings = []
known_names = []

def load_training_images():
    """Load and encode training images."""
    global known_encodings, known_names
    for file in TRAINING_IMAGES_PATH.iterdir():
        if file.suffix in [".jpg", ".png"]:
            image = face_recognition.load_image_file(file)
            encoding = face_recognition.face_encodings(image)[0]
            known_encodings.append(encoding)
            known_names.append(file.stem)
    print("Loaded training images:", known_names)

load_training_images()

@app.post("/register/")
async def register_user(name: str = Form(...), photo: UploadFile = File(...)):
    """Register a user by uploading their photo."""
    ext = photo.filename.split(".")[-1]
    file_path = TRAINING_IMAGES_PATH / f"{name}.{ext}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(photo.file, buffer)

    # Encode and add new face to the system
    image = face_recognition.load_image_file(file_path)
    encoding = face_recognition.face_encodings(image)[0]
    known_encodings.append(encoding)
    known_names.append(name)
    return {"message": f"User {name} registered successfully!"}

def generate_frames():
    """Generate video frames for face recognition."""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            if matches:
                best_match_index = np.argmin(face_distances)
                name = known_names[best_match_index]
                y1, x2, y2, x1 = [v * 4 for v in face_location]
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, name, (x1, y2 + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.get("/recognize/")
def recognize():
    """Stream real-time face recognition."""
    return StreamingResponse(generate_frames(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/", response_class=HTMLResponse)
def documentation():
    """Documentation webpage."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Face Recognition API</title>
        <style>
            body {
                margin: 0;
                font-family: 'Arial', sans-serif;
                background: radial-gradient(circle, #e0f7fa, #80deea);
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                transition: background 0.5s, color 0.5s;
            }
            .container {
                text-align: center;
                padding: 20px;
                background: rgba(255, 255, 255, 0.9);
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            }
            h1 {
                font-size: 2.5rem;
                color: #00796b;
            }
            form input, form button {
                margin: 10px 0;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ddd;
            }
            form button {
                background: #00796b;
                color: white;
                border: none;
                cursor: pointer;
                transition: 0.3s;
            }
            form button:hover {
                background: #004d40;
            }
            .dark-mode-toggle {
                position: fixed;
                bottom: 20px;
                right: 20px;
            }
            .dark-mode-toggle label {
                cursor: pointer;
                font-size: 1.5rem;
            }
            body.dark {
                background: radial-gradient(circle, #263238, #37474f);
                color: #fff;
            }
            body.dark .container {
                background: rgba(0, 0, 0, 0.8);
            }
            body.dark form button {
                background: #00897b;
            }
            body.dark form button:hover {
                background: #00574b;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 Face Recognition API</h1>
            <p>Welcome to the <strong>Face Recognition API</strong>. Register users and recognize faces in real-time.</p>
            <h2>Endpoints</h2>
            <ul>
                <li><code>POST /register/</code>: Register a user with a name and photo.</li>
                <li><code>GET /recognize/</code>: Real-time face recognition stream.</li>
            </ul>
            <h3>Register a User</h3>
            <form action="/register/" method="post" enctype="multipart/form-data">
                <input type="text" name="name" placeholder="Enter your name" required>
                <input type="file" name="photo" required>
                <button type="submit">Register</button>
            </form>
        </div>
        <div class="dark-mode-toggle">
            <input type="checkbox" id="dark-mode" onchange="toggleDarkMode()">
            <label for="dark-mode">🌙</label>
        </div>
        <script>
            const toggleDarkMode = () => {
                document.body.classList.toggle('dark');
            };
        </script>
    </body>
    </html>
    """
