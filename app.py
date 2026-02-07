# hard-4-proxy-confusion/app.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return "ok"

@app.route("/api/feedback", methods=["POST"])
def feedback():
    raw = request.get_data().decode(errors="ignore")

    # BUG: backend parses a second hidden request
    if "GET /internal/admin" in raw:
        return "CTF{hard_request_smuggling}"

    return "ok"

@app.route("/internal/admin")
def admin():
    return "admin panel"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
