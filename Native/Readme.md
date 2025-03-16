# Verbal Communication Skills Trainer

## Overview

This project is a Verbal Communication Skills Trainer that helps users enhance their speaking abilities using an AI-powered assistant. The system provides real-time feedback on communication skills via text and voice interactions, leveraging Meta LLaMA-2-7B, Whisper (Speech-to-Text), and Text-to-Speech (TTS) technologies.

## Features

- Chat Coach: AI-powered feedback on textual communication.

- Voice Coach: Speech-to-text conversion with AI-driven evaluation.

- Skill Training:

- Impromptu Speaking

- Storytelling

- Conflict Resolution

- Presentation Assessment: AI evaluation of speech or written presentations.

## Tech Stack

- Language Model: Meta LLaMA-2-7B-Chat

- Speech-to-Text: OpenAI Whisper

- Text-to-Speech: Mozilla TTS

- UI Framework: Streamlit

- Backend: Hugging Face Transformers, PyTorch
## Methodology 
![](methodologyjpg)

### Installation

- Prerequisites

Ensure that Python 3.11+ is installed and that your machine has a stable internet connection.

- Step 1: Clone the Repository

```bash git clone https://github.com/your-repository/verbal-skills-trainer.git
 cd verbal-skills-trainer
```
- Step 2: Create and Activate Virtual Environment
```bash python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```
- Step 3: Install Dependencies

```bash pip install --upgrade pip
pip install torch torchvision torchaudio transformers whisper TTS streamlit
```
- Step 4: Authenticate with Hugging Face

```bash huggingface-cli login```
Note: The Meta LLaMA models are gated, so you must accept their terms on Hugging Face before using them.

- Step 5: Run the Application

```bash streamlit run verbal_skills_trainer.py ```

##Methodology

1️⃣ Model Selection & Optimization

We use Meta LLaMA-2-7B-Chat for conversational analysis.

The model is quantized to 4-bit for memory efficiency using bitsandbytes.

MPS (Metal Performance Shaders) is enabled for Mac M1/M2 users.

2️⃣ Interactive Communication Modes

Chat-based evaluation of clarity, coherence, and tone.

Speech input processing via OpenAI Whisper.

TTS (Text-to-Speech) for spoken feedback.

3️⃣ Training & Assessment

Skill Training: AI-generated prompts assess response structure and effectiveness.

Presentation Analysis: AI scores speeches based on structure, delivery, and persuasiveness.

### Expected Outcomes

- Improved verbal clarity through AI feedback.

- Enhanced confidence in public speaking.

- Objective speech assessment for self-improvement.

### Troubleshooting

🔥 Model Not Found Error?

Ensure you are logged in to Hugging Face:
```bash
huggingface-cli login
```
Manually download the model:

```bash git lfs install
git clone https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
```
Update the script to use the local model path:
```bash
MODEL_NAME = "./Llama-2-7b-chat-hf"
```
🛠 Slow Performance?

Tried using LLaMA-2-7B instead of 70B.

Used 4-bit quantization (load_in_4bit=True).

Integration with more voice synthesis models.

🔥 LOW CPU SPACE
It requires above 130 gb CPU storage, but I am lacking with that.
I also can't do it through Google Colab
Trying using small models

