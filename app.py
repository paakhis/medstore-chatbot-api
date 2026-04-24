from flask import Flask, render_template, request, jsonify
from chatbot import CB

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    message = request.args.get("msg") or request.form.get("msg")
    
    if not message:
        return jsonify({"response": "Please enter a message."})

    msg = message.lower()

    # Controlled logic (important)
    if "hello" in msg or "hi" in msg:
        response = "Hi, welcome to MedStore Assistant!"

    elif "product" in msg:
        response = "We offer ECG machines, monitors, and diagnostic devices."

    elif "order" in msg:
        response = "Please provide your order ID to check status."

    elif "thank" in msg:
        response = "You're welcome!"

    else:
        # fallback to chatbot
        response = str(CB.get_response(message))

    return response


if __name__ == "__main__":
    app.run(debug=True)