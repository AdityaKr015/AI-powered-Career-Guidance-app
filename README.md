AI Career Guidance App

A simple Streamlit web app powered by Google Gemini API that provides career guidance and answers queries using AI.

🚀 Features

Interactive UI with Streamlit

Uses Google Pro AI (Gemini)

Secure API key handling with .env file

Easy to run locally

🛠️ Installation

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt


Setup environment variables:

Create a .env file in the project root.

Add your API key inside:

GOOGLE_API_KEY=your_api_key_here

▶️ Usage

Run the Streamlit app:

streamlit run app.py   ->"app.py" can be replace by the name of your file you gave


this opens http://localhost:8501 in your browser.Now you can use it.

📂 Project Structure
.
├── app.py
├── requirements.txt
├── .env.example
├── README.md

