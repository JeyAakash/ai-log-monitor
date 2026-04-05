from flask import Flask, render_template_string
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.model import predict_log

app = Flask(__name__)

logs = [
    "User logged in",
    "Database connection failed",
    "Timeout occurred"
]

@app.route("/")
def home():
    results = [(log, predict_log(log)) for log in logs]

    html = """
    <h2>AI Log Monitoring Dashboard</h2>
    <table border=1>
    <tr><th>Log</th><th>Status</th></tr>
    {% for log, status in results %}
    <tr>
        <td>{{log}}</td>
        <td>{{status}}</td>
    </tr>
    {% endfor %}
    </table>
    """
    return render_template_string(html, results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)