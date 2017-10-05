from flask import Flask,  make_response, request, render_template
import sys


app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1>Hello heroku</h1><p>Python: {ver}</p>".format(ver=sys.version)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
