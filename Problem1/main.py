import requests
import flask
from werkzeug.datastructures import MultiDict
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/numbers/', methods=['GET'])
def home():
    fl = []
    l = MultiDict(request.args)
    for i in l.getlist('url'):
        response = requests.get(str(i))
        fl.extend(response.json()['numbers'])
    d = {'numbers': sorted(set(fl))}
    return jsonify(d)


app.run()
