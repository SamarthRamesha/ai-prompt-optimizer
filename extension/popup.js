document.getElementById("optimizeBtn").addEventListener("click", async () => {
  const prompt = document.getElementById("prompt").value;

  const response = await fetch("http://127.0.0.1:8000/optimize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ prompt })
  });

  const data = await response.json();

  document.getElementById("output").textContent =
    `Role: ${data.role}
Task: ${data.task}
Context: ${data.context}
Output: ${data.output_format}`;
});