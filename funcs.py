import json


def write_json(data):
    try:
        with open("data.json", "w", encoding="utf8") as f:
            json.dump(data, f)

        return "True"
    except:
        return "False"


def read_json():
    with open("data.json", "r", encoding="utf8") as f:
        data = json.loads(f.read())

    return data
