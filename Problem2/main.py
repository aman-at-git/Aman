import requests
import flask
from werkzeug.datastructures import MultiDict
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

list = ['bonfire', 'cardio', 'case', 'character', 'bonsai']

@app.route('/prefixes/', methods=['GET'])
def home():
    l = str(request.args['keywords']).split(',')
    f = []
    for i in l:
        if i in list:
            # print()
            d = {
                 "keyword": i,
                 "status": "found",
                 "prefix": 'prefix'
            }
        else:
            d = {
                "keyword": i,
                "status": "not_found",
                "prefix": "not_applicable"
            }
        f.append(d)
    return jsonify(f)

app.run()
