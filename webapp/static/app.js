const btn = document.getElementById("runBtn");
const topicInput = document.getElementById("topic");
const statusEl = document.getElementById("status");
const outputEl = document.getElementById("output");


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
    data.result.forEach(article => {
      const articleEl = document.createElement("div");
      articleEl.classList.add("article");
      
      articleEl.innerHTML = `
        <h2><a href="${article.url}" target="_blank">${article.title}</a></h2>
	<p>${article.summary}</p>
      `;

      article.claims.forEach(claim => {
        const claimEl = document.createElement("div");
	claimEl.classList.add("claim", claim.verdict.toLowerCase().replace(" ", ""));

	const claimText = document.createElement("b");
	claimText.classList.add("claim-text", claim.verdict.toLowerCase().replace(" ", ""));
	claimText.textContent = `${claim.claim} - ${claim.verdict}`;
	claimEl.appendChild(claimText);

	const sourcesEl = document.createElement("div");
	claim.sources.forEach(source => {
	  const a = document.createElement("a");
	  a.href = source.url;
	  a.target = "_blank";
	  a.rel = "noopener noreferrer";
	  a.textContent = source.name || source.url;
	  sourcesEl.appendChild(a);
	  sourcesEl.appendChild(document.createTextNode(" | "));
	});

	if (sourcesEl.lastChild) sourcesEl.removeChild(sourcesEl.lastChild);

	claimEl.appendChild(sourcesEl);

	articleEl.appendChild(claimEl);
      });

      outputEl.appendChild(articleEl);
    });

  } catch (e) {
    statusEl.textContent = "Network error.";
  }
});
