# hard-4-proxy-confusion/app.py
from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
<h2>Feedback Gateway</h2>
<p>Public feedback ingestion API behind enterprise proxy.</p>
<ul>
<li>POST /api/feedback</li>
<li>GET /health</li>
</ul>
<p>All requests are logged and inspected.</p>
"""

@app.route("/health")
def health():
    return "ok"

@app.route("/api/feedback", methods=["POST"])
def feedback():
    raw = request.get_data().decode(errors="ignore")

    if "GET /internal/admin" in raw:
        return "CTF{hard_request_smuggling}"

    return "ok"

@app.route("/internal/admin")
def admin():
    return "admin panel"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
