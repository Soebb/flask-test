from stream import create_stream_url
from py_youtube import Data
from flask import Flask, request, render_template

app = Flask(__name__)

default_thumb = "https://github.com/Soebb/own-utube-stream-link-gen/raw/main/default_thumbnail.jpg"

@app.route('/')
def home():
   return 'Hello, my function is creating YouTube stream url.'
