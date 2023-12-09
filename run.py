from app import app

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = 'TU_API_KEY'  # Reemplaza con tu clave de API de OpenAI

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpt3', methods=['POST'])
def gpt3():
    if request.method == 'POST':
        prompt = request.form['prompt']
        response = generate_response(prompt)
        return render_template('index.html', prompt=prompt, response=response)

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Puedes elegir otro motor según tus necesidades
        prompt=prompt,
        max_tokens=100  # Ajusta según sea necesario
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
