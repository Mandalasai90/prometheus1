from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

REQUEST_COUNT = Counter("app_request_count", "Total number of requests made to the application")

app = Flask(__name__)

@app.route("/")
def hello_team():
    REQUEST_COUNT.inc()
    return "Hello Team, This is from Docker WSGI...."

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Note: When using tiangolo/uwsgi-nginx-flask, uWSGI runs the app.
# The block below is only for local debug runs (e.g., python app/main.py).
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
