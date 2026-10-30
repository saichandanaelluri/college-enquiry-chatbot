from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    question = request.form.get("msg", "").strip()
    if not question:
        return jsonify({"response": "Please type a question about SCSVMV."}), 400
    answer = get_response(question)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

