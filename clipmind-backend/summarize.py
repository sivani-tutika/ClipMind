import requests
import os
import openai

# Use Ollama locally
def generate_summary(text: str) -> str:
    prompt = f"Summarize the following text:\n\n{text[:4000]}"
    print("Using Ollama")
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"prompt": prompt, "model": "llama2", "stream": False}
        )
        # print("Response from Ollama:", response.json())
        print(response.json().get("response"))
        return response.json().get("response", "")
    except Exception as e:
        raise ValueError(f"Failed to summarize via Ollama: {e}")
    
def generate_summary_openai(text: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print("Using OpenAI")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Summarize the following text:\n\n{text[:4000]}"}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise ValueError(f"Failed to summarize via OpenAI: {e}")