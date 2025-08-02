import os
import streamlit as st
from openai import OpenAI

# Set environment variable from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

client = OpenAI()

def generate_commentary(play_text):
    prompt = f"""Convert the following boring sports play into exciting, human-like commentary.

Boring: {play_text}
Exciting:"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,
        max_tokens=60,
    )
    return response.choices[0].message.content.strip()

st.title("🏀 Sports Commentary Generator")

play_input = st.text_area("Enter a sports play description:", height=100)

if st.button("Generate Commentary"):
    if play_input.strip() == "":
        st.warning("Please enter a play description first!")
    else:
        with st.spinner("Generating commentary..."):
            commentary = generate_commentary(play_input)
            st.success("Here's your exciting commentary:")
            st.write(commentary)
