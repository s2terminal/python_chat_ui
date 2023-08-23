import streamlit
import openai

input_text = streamlit.text_input('入力')
if len(input_text) > 0:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_text}],
        max_tokens=100,
    )

    streamlit.write(completion["choices"][0]["message"]["content"])
