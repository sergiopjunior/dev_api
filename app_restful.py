from flask import Flask, request
from flask_restful import Resource, Api
from funcs import write_json, read_json
import json
import os

app = Flask(__name__)
api = Api(app)

developers = []
os.chdir(r".")
if "data.json" not in os.listdir():
    write_json(developers)
else:
    developers = read_json()


class Developer(Resource):

    def get(self, did):
        try:
            response = developers[did]
        except IndexError:
            response = "Developer ID not found."
        except Exception as e:
            response = {"Status": "Error", "Message": e}
        finally:
            return response

    def put(self, did):
        try:
            developers.append(json.loads(request.data))
            response = write_json(developers)
        except Exception as e:
            response = {"Status": "Error", "Message": e}
        finally:
            return response

    def patch(self, did):
        try:
            developers[did] = json.loads(request.data)
            response = write_json(developers)
        except IndexError:
            response = "Developer ID not found."
        except Exception as e:
            response = {"Status": "Error", "Message": e}
        finally:
            return response

    def delete(self, did):
        try:
            developers.pop(did - 1)
            response = write_json(developers)
        except IndexError:
            response = "Developer ID not found."
        except Exception as e:
            response = {"Status": "Error", "Message": e}
        finally:
            return response


class DevelopersList(Resource):

    def get(self):
        return developers


api.add_resource(Developer, "/dev/<int:did>")
api.add_resource(DevelopersList, "/dev/list")


if __name__ == '__main__':
    app.run(debug=True)