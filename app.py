from stream import create_stream_url
from py_youtube import Data
from flask import Flask, request, render_template

app = Flask(__name__)

default_thumb = "https://github.com/Soebb/own-utube-stream-link-gen/raw/main/default_thumbnail.jpg"

@app.route('/')
def hello():
   return 'Hello, my function is creating YouTube stream url.'

@app.route('/yt_stream')
def yt_stream():
   url = request.args.get('url')
   print("the requested url: "+url)
   url_data = Data(url)
   title = url_data.title()
   create_stream_url(url, title, default_thumb)
   return render_template(title+'.html')
