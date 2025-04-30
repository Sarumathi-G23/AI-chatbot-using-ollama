from flask import Flask, request, jsonify
import ollama  # Make sure you have ollama installed or accessible

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get('message', '')
    
    if not question:
        return jsonify({'response': 'Please ask something!'}), 400

    response = ollama.generate(model='gemma:2b', prompt=question)
    answer = response['response']
    
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
