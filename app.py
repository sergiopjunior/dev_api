from flask import Flask, request, jsonify
from funcs import write_json, read_json
import json
import os

app = Flask(__name__)

developers = []
os.chdir(r".")
if "data.json" not in os.listdir():
    write_json(developers)
else:
    developers = read_json()


@app.route("/dev", methods=["GET"])
def list_all():
    return jsonify(developers)


@app.route("/dev/<int:did>", methods=["GET", "PUT", "PATCH", "DELETE"])
def developer(did):
    if request.method == "GET":
        if 0 < did <= len(developers):
            return jsonify(developers[did - 1])
        else:
            return "Developer ID not found."
    elif request.method == "PUT":
        developers.append(json.loads(request.data))
        return write_json(developers)
    elif request.method == "PATCH":
        if 0 < did <= len(developers):
            developers[did - 1] = json.loads(request.data)
            return write_json(developers)
        else:
            return "Developer ID not found."
    elif request.method == "DELETE":
        if 0 < did <= len(developers):
            developers.pop(did - 1)
            return write_json(developers)
        else:
            return "Developer ID not found."


if __name__ == '__main__':
    app.run(debug=True)
