from flask import Flask, request, jsonify, redirect
import string
import random
import redis
import os

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(
    host=redis_host,
    port=redis_port,
    decode_responses=True
)

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    original_url = data.get('url')

    code = generate_code()
    r.set(code, original_url)

    return jsonify({
        "short_url": f"http://localhost:5000/{code}"
    })

@app.route('/<code>')
def redirect_url(code):
    original_url = r.get(code)
    if original_url:
        return redirect(original_url)
    return jsonify({"error": "URL not found"}), 404

