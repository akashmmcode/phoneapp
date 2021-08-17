import flask
import json
from flask import Flask, request, jsonify, Response


from helpers.get_all import get_all
from helpers.get_one import get_one
from helpers.post_add import post_add
from helpers.post_delete import post_delete
from helpers.post_update import post_update
from helpers.exceptions import ContactBookException, InputParamError
pyth

app = flask.Flask(__name__)
app.config["DEBUG"] = True
# _________________________________________________________________________________________________________________________


@app.route('/contacts/get-all', methods=["GET"])
def books_get_all():
    if request.method == 'GET':
        return get_all(request)
    else:
        "Nothing Found", 404
# _____________________________________________________________________________________________________________________________


@app.route('/contacts/get-one', methods=["GET"])
def books_get_one():
    try:
        if request.method == 'GET':
            return get_one(request)
    except KeyError as _e:
        return Response(
            json.dumps({"error": f"{_e} is missing"
                        }),
            status=400,
            mimetype="application/json")
    else:
        "Nothing Found", 404
# _________________________________________________________________________________________________________________________


@app.route('/contacts/post-add', methods=["POST"])
def books_addcontact():
    try:
        if request.method == 'POST':
            return post_add(request)
    except KeyError as _e:
        return Response(
            json.dumps({"error": f"{_e} is missing"
                        }),
            status=400,
            mimetype="application/json"
        )
    else:
        "Nothing Found", 404
# __________________________________________________________________________________________________________________________


@app.route('/contacts/delete', methods=["POST"])
def books_delcontact():
    try:
        if request.method == 'POST':
            return post_delete(request)
    except KeyError as _e:
        return Response(
            json.dumps({"error": f"{_e} is missing"
                        }),
            status=400,
            mimetype="application/json"
        )
    else:
        "Nothing Found", 404
# ______________________________________________________________________________________________________

@app.route('/contacts/update', methods=["POST"])
def books_updatecontact():
    try:
        if request.method == 'POST':
            return post_update(request)
    except KeyError as _e:
        return Response(
            json.dumps({"error": f"{_e} is missing"
                        }),
            status=400,
            mimetype="application/json"
        )
    else:
        "Nothing Found", 404


if __name__ == '__main__':
    app.run()
    