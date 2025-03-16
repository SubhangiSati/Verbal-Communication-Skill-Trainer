import os
import torch
import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# -----------------------------
# Configuration
# -----------------------------
SAVED_MODEL_PATH = "./saved_llama_model"  

device = "cuda" if torch.cuda.is_available() else "cpu"

# -----------------------------
# Load Trained Model
# -----------------------------
tokenizer = AutoTokenizer.from_pretrained(SAVED_MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(SAVED_MODEL_PATH).to(device)
generation_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("Verbal Communication Skills Trainer")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Chat Coach", "Training"])

# Chat Coach
if page == "Chat Coach":
    st.header("Chat Coach")
    user_input = st.text_area("Enter your text:")
    if st.button("Submit"):
        prompt = f"You are a communication coach. Analyze the following and provide feedback: {user_input}"
        response = generation_pipeline(prompt, max_length=200, temperature=0.7)[0]['generated_text']
        st.write("### Feedback:", response)

# Skill Training
elif page == "Training":
    st.header("Skill Training")
    training_prompts = {
        "impromptu": "Why is empathy important?",
        "storytelling": "Tell a short story about resilience.",
        "conflict_resolution": "How would you respond if your teammate is frustrated?"
    }
    skill_type = st.selectbox("Choose Training Type", list(training_prompts.keys()))
    if st.button("Start Training"):
        st.write("### Prompt:", training_prompts[skill_type])

if __name__ == "__main__":
    st.write("Start using the Verbal Communication Skills Trainer!")
