import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(question, context):
    prompt = f"""
    Answer the question using the following context only:

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
