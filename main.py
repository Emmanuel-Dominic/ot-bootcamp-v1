import json
from flask import Flask, jsonify, request, make_response
from model import users_db

app = Flask(__name__)


@app.route("/")
def welcome():
    return "You're welcome"


# @app.route("/users/<int:index>", methods=["GET"])
@app.route("/users/<int:index>")
def get_user(index):
    return jsonify({'user': users[index]})


@app.route("/users", methods=["POST", "GET"])
def users():
    if request.method == "POST":
        users_db.append(request.json["name"])
        resp = jsonify({"message": "successfully created!", "data": users_db})
        resp.status_code = 201
    else:
        resp = jsonify({"data": users_db})
        resp.status_code = 200
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
