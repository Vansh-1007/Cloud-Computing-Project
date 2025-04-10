from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "")

        prompt = f"### Instruction:\n{user_input}\nBe brief and concise.\n\n### Response:"

        payload = {
            "inputs": prompt,
            "parameters": {
                "temperature": 0.5,
                "max_new_tokens": 50,
                "return_full_text": False
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        response_json = response.json()
        print("Hugging Face response:", response_json)

        generated_text = ""

        if isinstance(response_json, list) and "generated_text" in response_json[0]:
            generated_text = response_json[0]["generated_text"]
        elif isinstance(response_json, dict) and "generated_text" in response_json:
            generated_text = response_json["generated_text"]
        else:
            generated_text = "Sorry, couldn't generate a response."

        return jsonify({"response": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
