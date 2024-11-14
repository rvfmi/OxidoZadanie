import openai
import os

key = os.getenv('OPENAI_API_KEY_RAFALM')

openai.api_key = key

default_file_path = "sample_article.txt"

prompt_file_path = "prompt.txt"

with open(default_file_path, 'r', encoding='utf-8') as file:
    article_content = file.read()

with open(prompt_file_path, 'r', encoding='utf-8') as file:
    prompt = file.read()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Jesteś asystentem pomagającym w generowaniu kodu HTML."},
        {"role": "user", "content": f"{prompt}\n{article_content}"}
    ],
    max_tokens=1500
)
generated_html = response['choices'][0]['message']['content']

with open('artykul.html', 'w', encoding='utf-8') as output_file:
    output_file.write(generated_html)
    