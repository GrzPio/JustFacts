const btn = document.getElementById("runBtn");
const topicInput = document.getElementById("topic");
const statusEl = document.getElementById("status");
const outputEl = document.getElementById("output");

btn.addEventListener("click", async () => {
  const topic = topicInput.value.trim();
  if (!topic) {
    statusEl.textContent = "Please enter a topic.";
    return;
  }

  statusEl.textContent = "Running pipeline... (this may take a bit)";
  outputEl.textContent = "";

  try {
    const res = await fetch(`/api/run?topic=${encodeURIComponent(topic)}`);
    const data = await res.json();

    if (!res.ok) {
      statusEl.textContent = data.error || "Error";
      return;
    }

    statusEl.textContent = `Done for topic: ${data.topic}`;
    outputEl.textContent = data.result;
  } catch (e) {
    statusEl.textContent = "Network error.";
  }
});
