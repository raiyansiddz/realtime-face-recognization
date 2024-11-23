# Face Recognition API

Welcome to the **Face Recognition API** project! This API allows you to register users and perform real-time face recognition using your webcam. Built with **FastAPI** and leveraging the power of the `face_recognition` library, this application provides an easy-to-use interface for detecting and identifying faces.

---

## 🚀 Features

- **Register Users**: Upload user images with names to the system and register them for future recognition.
- **Real-Time Face Recognition**: Use a webcam to stream live recognition and detect registered users.
- **Interactive Web UI**: Responsive interface with beautiful design and minimalistic UI.
- **Multi-Language Support**: Example code and documentation in various programming languages such as Python, JavaScript, Node.js, and more.
- **Easy Integration**: Comprehensive, easy-to-follow instructions for integrating the API with your own applications.

---

## 📋 Requirements

### System Requirements

- Python 3.8 or higher
- A webcam (for real-time recognition)

### Python Dependencies

To install all required dependencies, run:

```bash
pip install fastapi uvicorn face_recognition opencv-python numpy
Hardware
Webcam to use real-time recognition.
🔧 Installation & Setup
1. Clone the Repository
Start by cloning the repository:

bash
Copy code
git clone https://github.com/RaiyanSiddique/Face-Recognition-API.git
cd Face-Recognition-API
2. Install Dependencies
Next, install the dependencies using:

bash
Copy code
pip install -r requirements.txt
3. Run the Application
Start the FastAPI server with:

bash
Copy code
uvicorn main:app --reload
4. Open the Web UI
Once the server is running, open your browser and visit the following URL:

arduino
Copy code
http://127.0.0.1:8000
⚡ API Endpoints
1. /register/ (POST)
Register a new user by uploading their name and photo.

Request Parameters:
name: The name of the user (string).
photo: The image of the user (file upload).
Example (Python):
python
Copy code
import requests

url = "http://127.0.0.1:8000/register/"
files = {"photo": open("path_to_image.jpg", "rb")}
data = {"name": "John"}

response = requests.post(url, data=data, files=files)
print(response.json())
Success Response:
json
Copy code
{
  "message": "User John registered successfully!"
}
2. /recognize/ (GET)
This endpoint streams live video from your webcam and performs face recognition in real time.

How to Use:
Open your browser and visit the URL below to view live face recognition in action.
arduino
Copy code
http://127.0.0.1:8000/recognize/
Notes:
This endpoint requires a webcam to be connected and working.
The recognition will automatically display names of recognized users, if their faces were previously registered.
👨‍💻 Developer Information
Developer: Raiyan Siddique
GitHub: https://github.com/RaiyanSiddique
📄 License
MIT License

yaml
Copy code

This version uses clear sections with headings and has some inline code for commands and API responses to keep it neat and easy to follow. When pasted into GitHub, this markdown file will be nicely rendered and structured.

--- 

Let me know if you'd like any further modifications!
