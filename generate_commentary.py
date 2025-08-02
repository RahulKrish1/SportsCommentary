import os
from openai import OpenAI

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

# Test
if __name__ == "__main__":
    play = "Stephen Curry makes a 3-point jumper from the top of the key."
    print("Boring:", play)
    print("Exciting:", generate_commentary(play))