from flask import Flask, render_template, request, jsonify
from chatbot import get_response
from Code.hypertension import detect_hypertension

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    question = data['question']
    
    # Cek apakah pertanyaan berisi "#st" atau "#dt" untuk deteksi hipertensi
    if "#st" in question or "#dt" in question:
        response = detect_hypertension(question)
    else:
        response = get_response(question)
    
    return jsonify({'answer': response})

if __name__ == '__main__':
    app.run(debug=True)
