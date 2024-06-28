from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Initialize models
model_pipelines = {
    "model1": pipeline("question-answering", model="distilbert-base-cased-distilled-squad"),
    "model2": pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
}

current_model = model_pipelines["model1"]

@app.route('/answer', methods=['POST'])
def answer():
    data = request.json
    question = data['question']
    context = data['context']
    result = current_model(question=question, context=context)
    return jsonify(result)

@app.route('/switch_model', methods=['POST'])
def switch_model():
    global current_model
    model_name = request.json['model_name']
    if model_name in model_pipelines:
        current_model = model_pipelines[model_name]
        return jsonify({"status": "success", "model": model_name})
    else:
        return jsonify({"status": "error", "message": "Model not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
