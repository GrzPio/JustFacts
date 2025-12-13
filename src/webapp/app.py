from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

# Import your existing pipeline pieces
from src.crew.agents import build_agents
from src.crew.tasks import build_tasks
from crewai import Crew

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/api/run")
def run_pipeline():
    topic = request.args.get("topic", "").strip()
    if not topic:
        return jsonify({"error": "Missing topic parameter"}), 400

    news_agent, summarization_agent, fact_checking_agent = build_agents()
    tasks = build_tasks(topic, news_agent, summarization_agent, fact_checking_agent)

    crew = Crew(
        agents=[news_agent, summarization_agent, fact_checking_agent],
        tasks=tasks
    )

    # Crew output is usually a big text blob. Return it as-is first (simple).
    result_text = crew.run()

    return jsonify({
        "topic": topic,
        "result": str(result_text)
    })

if __name__ == "__main__":
    app.run(debug=True)
