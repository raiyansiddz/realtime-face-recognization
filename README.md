
Face Recognition API
A modern Face Recognition API built using FastAPI to register users and perform real-time face recognition using webcam feeds. This project uses the face_recognition library for efficient face detection and identification.

Features
Register Users: Upload user images along with a name to the system.
Real-Time Face Recognition: Detect faces and identify registered users via a webcam stream.
Modern Web UI: A responsive, developer-friendly interface with example code snippets for multiple programming languages.
API Documentation: Includes detailed API usage instructions and examples for Python, JavaScript, Node.js, and more.
Requirements
System Requirements
Python 3.8 or higher
A webcam (for real-time recognition)
Python Dependencies
Install the dependencies using pip:

bash
Copy code
pip install fastapi uvicorn face_recognition opencv-python numpy
Usage
1. Clone the Repository
bash
Copy code
git clone https://github.com/RaiyanSiddique/Face-Recognition-API.git
cd Face-Recognition-API
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the Application
Start the FastAPI server:

bash
Copy code
uvicorn main:app --reload
4. Access the Web Interface
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:8000
Endpoints
1. /register/ (POST)
Registers a new user with their name and image.

Request
Form Data:
name: User's name (string)
photo: User's photo (file)
Example (Python Code)
python
Copy code
import requests

url = "http://127.0.0.1:8000/register/"
files = {"photo": open("path_to_image.jpg", "rb")}
data = {"name": "John"}

response = requests.post(url, data=data, files=files)
print(response.json())
2. /recognize/ (GET)
Streams real-time webcam feed for face recognition.
This endpoint opens a live video feed in your browser where it detects and identifies previously registered users.

Usage Instructions
Open your browser and navigate to the following link:
arduino
Copy code
http://127.0.0.1:8000/recognize/
Allow webcam access if prompted by the browser.
Live Recognition: The feed will display bounding boxes and names of registered users detected in the frame.
Important Notes
Ensure you have registered at least one user via /register/ before using /recognize/.
Use a webcam with good lighting for accurate results.
Project Structure
bash
Copy code
Face-Recognition-API/
├── main.py              # Main FastAPI application
├── training_images/     # Directory for storing user photos
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
UI Features
Gradient Background: A subtle gradient to enhance visual appeal.
Dynamic Buttons: Hover effects for better interactivity.
Responsive Design: Works seamlessly on both desktop and mobile devices.
Code Examples: Pre-built API request examples for developers.
API Examples
Register User (Python)
python
Copy code
import requests

url = "http://127.0.0.1:8000/register/"
files = {"photo": open("path_to_image.jpg", "rb")}
data = {"name": "John"}

response = requests.post(url, data=data, files=files)
print(response.json())
Start Recognition
Open a browser and navigate to:
arduino
Copy code
http://127.0.0.1:8000/recognize/
Watch as registered users are identified in real time.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributors
Developed by Raiyan Siddique
Feel free to contribute to this project by submitting issues or pull requests!

MIT License
sql
Copy code
MIT License

Copyright (c) 2024 Raiyan Siddique

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
