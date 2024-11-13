import openai
import os

key = os.getenv('OPENAI_API_KEY_RAFALM')

openai.api_key = key

default_file_path = "sample_article.txt"

with open(default_file_path, 'r', encoding='utf-8') as file:
    article_content = file.read()

prompt = (
    "Proszę wygenerować kod HTML na podstawie poniższego artykułu. Kod powinien spełniać następujące wytyczne:\n"
    "1. Struktura treści powinna być sformatowana przy użyciu odpowiednich tagów HTML.\n"
    "2. Tam, gdzie warto wstawić ilustracje dla urozmaicenia treści, proszę wstawić tag <img> "
    "z atrybutem src ustawionym na 'image_placeholder.jpg'. Proszę także dodać atrybut 'alt' "
    "do każdego obrazka, zawierający dokładny prompt, który można użyć do wygenerowania odpowiedniej grafiki."
    "Prompt powinien być rozbudowany i różnić się od podpisu\n"
    "3. Dla każdej ilustracji proszę również dodać krótki podpis, umieszczony pod obrazkiem, używając odpowiedniego tagu HTML.\n"
    "4. Wygenerowany kod HTML powinien zawierać wyłącznie zawartość do umieszczenia pomiędzy tagami <body> i </body>. "
    "Nie należy dołączać tagów <html>, <head> ani <body>. Proszę nie stosować stylów CSS ani JavaScript.\n"
    "\n\nOto treść artykułu:\n\n"
)
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
    