from datetime import datetime, timedelta
from flask import Flask, request, jsonify

app = Flask(__name__)

# Number of requests allowed in a time period
RATE_LIMIT = 1000
# Time period for rate limit
TIME_PERIOD = 60

# Store the number of requests made and the time of the first request
request_count = 0
first_request_time = None

@app.route("/app")
def index():
    global request_count, first_request_time

    # Get the current time
    now = datetime.now()

    # Check if the rate limit has been reached
    if request_count >= RATE_LIMIT:
        # Check if the time period has passed
        if now - first_request_time < timedelta(seconds=TIME_PERIOD):
            # Return a 429 response with the rate limit information
            return jsonify({"error": "Too Many Requests"}), 429, {
                "X-Rate-Limit": RATE_LIMIT,
                "X-Wait-Till": (first_request_time + timedelta(seconds=TIME_PERIOD)).strftime("%Y-%m-%d %H:%M:%S"),
            }
    # Increment the request count
    request_count += 1

    # Set the first request time if it has not been set
    if first_request_time is None:
        first_request_time = now

    # Return the request count
    return jsonify({"request_count": request_count})

if __name__ == "__main__":
    app.run()
