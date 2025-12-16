from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from justfacts.crew import Justfacts
import json

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
    result = crew.kickoff(inputs={"topic": topic})

    result_json = json.loads(result.raw)

    return jsonify({
        "topic": topic,
        "result": result_json
    })

if __name__ == "__main__":
    app.run(debug=True)
