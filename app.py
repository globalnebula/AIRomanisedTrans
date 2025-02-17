import streamlit as st
from groq import Groq

def translate_text(text, model="llama3-8b-8192"):
    client = Groq(api_key="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")
    completion = client.chat.completions.create(
        model= "llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a translator that converts romanized Telugu to English."},
            {"role": "user", "content": text}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    translated_text = ""
    for chunk in completion:
        translated_text += chunk.choices[0].delta.content or ""
        yield translated_text

st.title("Romanized Telugu to English Translator")
user_input = st.text_input("Enter text in romanized Telugu :")

if user_input:
    st.write("### Translation:")
    translation_area = st.empty()
    
    translated_text = ""
    for chunk in translate_text(user_input):
        translated_text = chunk
        translation_area.write(translated_text)