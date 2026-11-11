🌍 Language Translator Tool

Project Overview
The Language Translator Tool is a Python-based web application developed as part of the CodeAlpha Artificial Intelligence Internship.
This application allows users to translate text from one language to another using the MyMemory Translation API. It provides a simple and user-friendly interface built with Streamlit.
✨ Features
 - Translate text between multiple languages.
 - Select source and target languages.
 - Real-time translation using MyMemory API.
 - Display translated text clearly.
 - Copy translated text using the copy option.
 - Text-to-Speech functionality to listen to translated text.
 - Simple and user-friendly interface.

🛠️ Technologies Used

 - Python
 - Streamlit
 - MyMemory Translation API
 - Requests
 - gTTS (Google Text-to-Speech)

📂 Project Structure

Language_Translator_Tool/
│
├── app.py
├── requirements.txt
└── README.md

⚙️ Installation and Setup

1. Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_LINK

2. Navigate to the Project Folder

cd Language_Translator_Tool

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

streamlit run app.py

The application will open in your browser at:

"http://localhost:8501"

🌐 API Used

MyMemory Translation API

Official Documentation: https://mymemory.translated.net/doc/spec.php

The application uses the API to send text and receive translated results. An API key is not required for basic usage.

🔊 Text-to-Speech

The application uses gTTS to convert translated text into speech so users can listen to the translation.

📌 Requirements

- Python 3.x
- Internet connection
- Required Python libraries

👨‍💻 Internship Project

Organization: CodeAlpha

Task: Language Translation Tool

Domain: Artificial Intelligence

📝 Author

Muhammad Imran Shah

Project: Language Translator Tool

---
Developed as part of the CodeAlpha Artificial Intelligence Internship.
