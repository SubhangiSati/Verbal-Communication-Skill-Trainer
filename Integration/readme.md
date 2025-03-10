# Verbal Communication Skills Trainer (INTEGRATION USING API)

## Overview
This project is a **Verbal Communication Skills Trainer** built using **Streamlit** and **Azure OpenAI GPT-4o**. The application helps users improve their verbal communication skills through **interactive chat, voice analysis, skill training activities, and presentation assessments**.

## Features
- **Chat with AI Coach**: Get feedback on clarity and effectiveness of communication.
- **Voice Input Analysis**: Upload a `.wav` file and receive AI-driven feedback.
- **Skill Training Activities**:
  - **Impromptu Speaking**: Get evaluated on spontaneous speaking ability.
  - **Storytelling**: Improve narrative structure and engagement.
  - **Conflict Resolution**: Receive feedback on handling difficult conversations.
- **Presentation Assessment**: AI analyzes presentation structure, content, and delivery.
- **User Progress Tracking**: Stores user responses and AI feedback in an SQLite database.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python (Flask-like logic in Streamlit)
- **AI Model**: Azure OpenAI GPT-4o
- **Database**: SQLite
- **Speech Processing**: SpeechRecognition (Google Speech-to-Text)
- **Text-to-Speech**: pyttsx3

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/verbal-communication-trainer.git
cd verbal-communication-trainer
```
###2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
###3️⃣ Set Up Environment Variables

Create a .env file and add your Azure OpenAI API key:

GITHUB_TOKEN=your_azure_openai_api_key_here

###4️⃣ Run the Application
```bash
streamlit run app.py
```
##Usage Guide

-Chat with AI Coach: Enter a message and get structured feedback.

-Voice Input Analysis: Upload a .wav file to receive AI feedback.

-Skill Training: Select an activity, enter a response, and receive AI feedback.

-Presentation Assessment: Paste a presentation script for analysis.

-View Progress: Review stored responses and feedback.

##Example Prompts

- "How can I sound more confident in my speech?"
- "Analyze my storytelling: Once upon a time, a boy found a mysterious map…"
- "Evaluate my impromptu speaking: Why is teamwork important?"


Advanced sentiment analysis for emotional feedback.

