import streamlit as st
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt, model="mistral"):
    response = requests.post(OLLAMA_URL, json={"model": model, "prompt": prompt}, stream=True)
    response_text = ""
    for line in response.iter_lines():
        if line:
            try:
                json_line = line.decode("utf-8")
                data = json.loads(json_line)
                response_text += data.get("response", "")
            except Exception:
                continue
    return response_text if response_text else "No response"

st.title("Ollama Chat via Streamlit")
user_input = st.text_input("Enter your query:")

if user_input:
    result = query_ollama(user_input)
    st.write("Response from Ollama:")
    st.write(result)