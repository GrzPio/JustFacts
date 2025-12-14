const btn = document.getElementById("runBtn");
const topicInput = document.getElementById("topic");
const statusEl = document.getElementById("status");
const outputEl = document.getElementById("output");

function getVerdictColor(verdict) {
  if (verdict == "verified") return "green";
  if (verdict == "partially_verified") return "orange";
  if (verdict == "unverified") return "red";
  return "black";
}

btn.addEventListener("click", async () => {
  const topic = topicInput.value.trim();
  if (!topic) {
    statusEl.textContent = "Please enter a topic to search.";
    return;
  }

  statusEl.textContent = "Running pipeline...";
  outputEl.innerHTML = "";

  try {
    const res = await fetch(`/api/run?topic=${encodeURIComponent(topic)}`);
    const data = await res.json();

    if (!res.ok) {
      statusEl.textContent = data.error || "Error";
      return;
    }

    statusEl.textContent = `Done for topic: ${data.topic}`;
    outputEl.textContent = data.result;
    data.result.forEach(article => {
      const articleEl = document.createElement("div");
      
      articleEl.innerHTML = `
        <h2>${article.title}</h2>
	<p>${article.summary}</p>
      `;

      article.claims.forEach(claim => {
        const claimEl = document.createElement("div");
	claimEl.innerHTML = `
	  <b style="color:${getVerdictColor(claim.verdict)}">
	    ${claim.text} - ${claim.verdict}
	  </b>
	  <div>Sources: ${claim.source.join(", ")}</div>
	`;
	claimEl.classList.add("claim", verdict.toLowerCase().replace(" ", ""));

	articleEl.appendChild(claimEl);
      });

      outputEl.appendChild(articleEl);
    });

  } catch (e) {
    statusEl.textContent = "Network error.";
  }
});
