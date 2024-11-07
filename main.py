from flask import Flask, request, send_file
from datetime import datetime
import logging
import os
import requests

app = Flask(__name__)

# Set up logging (you can modify this to log to a file or database)
logging.basicConfig(level=logging.INFO)

def get_location():
    """Fetch location data based on the IP address."""
    response = requests.get("https://ipinfo.io")
    if response.status_code == 200:
        return response.json()
    return None

# Endpoint for serving the tracking pixel
@app.route('/pixel', methods=['GET'])
def tracking_pixel():
    """Serve the 1x1 tracking pixel and log the email open event."""
    # Extract query parameters from the request
    

    

    # Log the complete event details
    logging.info(f"Complete log entry: {get_location()}")

    # Serve a transparent 1x1 pixel image
    pixel_path = "Image\\white.png"  # Absolute path to the image on PythonAnywhere
    if os.path.exists(pixel_path):
        return send_file(pixel_path, mimetype='image/png')
    else:
        logging.error("Pixel image not found.")
        return "Pixel image not found", 404
app.run(debug=True)
# Note: app.run() is not needed on PythonAnywhere since WSGI will handle running the app.
