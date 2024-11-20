from flask import Flask, request, send_file
from pytracking.tracking import EmailTracking

app = Flask(__name__)
tracking = EmailTracking(base_url="https://yourdomain.com")


@app.route('/track/<tracking_id>')
def track(tracking_id):
    # Log or process tracking info
    print(f"Email opened! Tracking ID: {tracking_id}")
    # Return a 1x1 transparent pixel
    return send_file("pixel.png", mimetype="image/png")


if __name__ == "__main__":
    app.run()
