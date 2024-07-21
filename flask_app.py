from flask import Flask, jsonify
import redis
import os
app = Flask(__name__)


# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
cache = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)


@app.route("/")
def hello():
    count = cache.incr("hits")
    return jsonify(message=" This Is a Flask App Made by David Paul!", hits=count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
