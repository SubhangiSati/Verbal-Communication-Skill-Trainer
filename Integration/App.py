import os
import json
import sqlite3
import streamlit as st
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from openai import OpenAI  

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI API Key
AZURE_API_KEY = os.getenv("GITHUB_TOKEN")
AZURE_ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "gpt-4o"

# Initialize SQLite database
DB_NAME = "verbal_skills.db"
conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    activity TEXT,
    response TEXT,
    feedback TEXT
)
''')
conn.commit()

# Speech Recognizer
recognizer = sr.Recognizer()

# Text-to-Speech Engine
tts_engine = pyttsx3.init()

def format_feedback(feedback):
    """Format AI response to be human-readable."""
    feedback = feedback.replace("### Strengths:", "\n\n**Strengths:**")
    feedback = feedback.replace("### Areas for Improvement:", "\n\n**Areas for Improvement:**")
    feedback = feedback.replace("### Revised Example:", "\n\n**Revised Example:**")
    feedback = feedback.replace("**", "")  # Remove bold markers
    feedback = feedback.replace("\n-", "\n•")  # Convert dashes to bullet points
    feedback = feedback.replace("\n1.", "\n1)").replace("\n2.", "\n2)").replace("\n3.", "\n3)").replace("\n4.", "\n4)")  # Fix numbering
    return feedback.strip()

def generate_ai_response(prompt):
    """Send prompt to Azure OpenAI API and get a response."""
    client = OpenAI(base_url=AZURE_ENDPOINT, api_key=AZURE_API_KEY)  

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,  
            messages=[
                {"role": "system", "content": "You are an AI communication coach. Provide clear, human-readable feedback without markdown formatting."},
                {"role": "user", "content": prompt}
            ],
            stream=False 
        )
        return format_feedback(response.choices[0].message.content.strip())
    except IndexError:
        return "Error: No response received from the AI model. Please try again."

# Streamlit UI
st.title("Verbal Communication Skills Trainer")

# Chat Interaction
st.header("Chat with AI Coach")
user_input = st.text_input("Enter your message:")
if st.button("Send Message"):
    if user_input:
        response = generate_ai_response(f"Assess my verbal clarity: {user_input}")
        st.write("**AI Feedback:**", response)

# Voice Input Processing
st.header("Voice Input Analysis")
uploaded_file = st.file_uploader("Upload a .wav file", type=["wav"])
if uploaded_file is not None:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    with sr.AudioFile("temp_audio.wav") as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            feedback = generate_ai_response(f"Analyze my speech delivery: {text}")
            st.write("**Transcription:**", text)
            st.write("**AI Feedback:**", feedback)
        except sr.UnknownValueError:
            st.write("Could not understand the audio.")

# Skill Training
st.header("Skill Training Activities")
activity = st.selectbox("Choose an activity:", ["impromptu_speaking", "storytelling", "conflict_resolution"])
response_text = st.text_area("Enter your response:")
if st.button("Submit Response"):
    prompt_map = {
        "impromptu_speaking": "Assess my impromptu speaking on this topic:",
        "storytelling": "Critique my storytelling structure:",
        "conflict_resolution": "Evaluate my conflict resolution skills:"
    }
    feedback = generate_ai_response(f"{prompt_map[activity]} {response_text}")
    cursor.execute("INSERT INTO user_progress (user, activity, response, feedback) VALUES (?, ?, ?, ?)",
                   ("User1", activity, response_text, feedback))
    conn.commit()
    st.write("**AI Feedback:**", feedback)

# Presentation Assessment
st.header("Presentation Assessment")
presentation_text = st.text_area("Enter your presentation script:")
if st.button("Evaluate Presentation"):
    feedback = generate_ai_response(f"Evaluate my presentation script: {presentation_text}")
    st.write("**AI Feedback:**", feedback)

# View Progress
st.header("User Progress")
if st.button("View Progress"):
    cursor.execute("SELECT * FROM user_progress")
    records = cursor.fetchall()
    for record in records:
        formatted_feedback = format_feedback(record[4])  
        st.write(f"**Activity:** {record[2]}")
        st.write(f"**Response:** {record[3]}")
        st.write(f"**Feedback:** {formatted_feedback}")
        st.write("---")