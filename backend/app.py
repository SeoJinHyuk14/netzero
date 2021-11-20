import os

import requests
from flask import Flask, jsonify
from flask_cors import CORS

ENV = os.environ.get('ENV', 'dev')
YOUTUBE_API_TOKEN = os.environ.get('YOUTUBE_API_TOKEN', '')
app = Flask(__name__)
cors = CORS(
  app,
  resources={r"/*": {"origins": "*"}}
)


@app.route('/')
def index():
  url = f"https://www.googleapis.com/youtube/v3/videos?id=0a7y1DEuASM&key={YOUTUBE_API_TOKEN}&part=statistics"
  response = requests.get(url)
  result = response.json()

  return jsonify(result['items'][0]['statistics'])


if __name__ == "__main__":
  app.run(debug=True if ENV == 'dev' else False)
