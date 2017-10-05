# -*- coding: utf-8 -*-
from flask import Flask,  make_response, request, render_template
import sys
import json

app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1>Hello heroku</h1><p>Python: {ver}</p>".format(ver=sys.version)


@app.route('/webhook')
def webhook():
    req = request.get_json(silent=True, force=True)
    req_dump = json.dumps(req, indent=4)
    print('Request:\n{0}'.format(req_dump))

    speech = 'gwóźdź'
    response = {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "mr-muscle-bot"
    }

    response = json.dumps(response, indent=4)
    print('Response:\n{0}'.format(response))

    r = make_response(response)
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
