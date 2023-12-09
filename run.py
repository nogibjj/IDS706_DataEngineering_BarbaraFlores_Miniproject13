from flask import Flask, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = Flask(__name__)

@app.route('/')
def home():
    # Cargar modelo y tokenizador
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Generar texto con el modelo
    input_text = "Escribe aquí tu texto de entrada..."
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=50, num_beams=5, no_repeat_ngram_size=2, top_k=50, top_p=0.95, temperature=0.7)

    # Decodificar y renderizar el resultado
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return render_template('index.html', generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
