from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from src.justfacts.crew import Justfacts

load_dotenv()

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/run")
def run_pipeline():
    topic = request.args.get("topic", "").strip()
    if not topic:
        return jsonify({"error": "Missing topic parameter"}), 400

    crew = Justfacts().crew()
    result = crew.run(inputs={"topic": topic})

    return jsonify({
        "topic": topic,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
