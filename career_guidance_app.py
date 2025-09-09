import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini with the API key
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro-002")

st.set_page_config(page_title="AI Career Guidance",layout="centered")
st.title("AI Career Guidance for Students")
st.markdown("Get personalized career suggestions based on your interests and skills!")

with st.form("career_form"):
    name = st.text_input("Your Name")
    grade = st.selectbox("Your Current Class/Grade",["10th","11th","12th","Undergraduate","Postgraduate","Other"])
    subjects = st.text_area("Subjects and Marks (eg, Math: 90,Physics: 85 or CGPA etc)")
    interests = st.text_area("Your Interests (eg, coding, biology, design, public speaking, traveling and many more)")
    skills = st.text_area("Your Skills (eg, Python, drawing, teamwork)")
    personality=st.text_area("Personality (eg, Introvert, Extrovert)")
    goals = st.text_area("Career Goals (if any)")

    submit = st.form_submit_button("Get Career Guidance")

if submit:
    with st.spinner("🧠 Thinking deeply about your future... 🚀"):
        prompt = f"""
        You are an expert career counselor.

        Important Instructions:
        - First, check if the input has any Hindi words (like 'padhna', 'daudana', 'khelna') written in Roman script.
        - Even if English proportion is high, but any Hindi words exist, TREAT the whole input as Hinglish.
        - Hinglish means replying in a natural mix of Hindi and English, using Roman script (not Devanagari).
        - If 100% English input, reply in English.
        - If 100% Hindi in Devanagari script, reply in Hindi.
        - Do NOT change the user's original language feel.

        Student Profile:
        Name: {name}
        Class: {grade}
        Subjects and Marks: {subjects}
        Interests: {interests}
        Skills: {skills}
        Personality: {personality}
        Career Goals: {goals}

        Response Instructions:
        - Suggest Top 5 career paths.
        - Recommend suitable stream.
        - Suggest important skills to develop.
        - Give future opportunities.
        - Keep tone sweet, motivating and friendly.
        - Use natural Hinglish phrasing if Hinglish detected (example: "tumhe coding aur design me career banana chahiye").

        Start responding now.
        """


        try:
            response = model.generate_content(prompt)
            st.success("Here's your personalized career guidance:")
            st.markdown(response.text)
        except Exception as e:
            st.error("Something went wrong while generating guidance. Please check your API key or try again later.")
            st.exception(e)

#If it doesn't run and gives MainThread missing errors then,run this in terminal -> "streamlit run career_guidance_app.py",Thanks😉