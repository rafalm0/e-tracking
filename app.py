from flask import Flask, Response
import pytracking

app = Flask(__name__)

# Generate tracking pixel in memory
pixel_data, mime_type = pytracking.get_open_tracking_pixel()


@app.route('/track/<tracking_data>')
def track(tracking_data):
    # Log that an email was opened
    print(f"Email opened! Tracking data: {tracking_data}")
    return Response(pixel_data, mimetype=mime_type)


if __name__ == '__main__':
    app.run()
