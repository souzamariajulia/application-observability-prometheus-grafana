
from flask import Flask, jsonify, Response, request, g
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Contador de todas as requisicoes HTTP
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total de requisicoes HTTP",
    ["method", "endpoint", "http_status"]
)

# Contador de requisicoes que retornaram erro 5xx
ERROR_COUNT = Counter(
    "http_errors_total",
    "Total de erros HTTP 5xx",
    ["endpoint"]
)

# Histograma para medir o tempo de resposta
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Tempo de resposta das requisicoes",
    ["endpoint"]
)


@app.before_request
def start_timer():
    g.start_time = time.perf_counter()


@app.after_request
def record_metrics(response):
    endpoint = request.endpoint or "unknown"

    duration = time.perf_counter() - g.start_time

    REQUEST_COUNT.labels(
        request.method,
        endpoint,
        str(response.status_code)
    ).inc()

    REQUEST_LATENCY.labels(endpoint).observe(duration)

    if response.status_code >= 500:
        ERROR_COUNT.labels(endpoint).inc()

    return response


@app.route("/")
def home():
    return jsonify({
        "message": "Aplicacao funcionando!",
        "status": "healthy"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/slow")
def slow():
    time.sleep(1.5)
    return jsonify({"message": "Resposta lenta"})


@app.route("/simulate-error")
def simulate_error():
    return jsonify({"error": "Erro simulado"}), 500


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
