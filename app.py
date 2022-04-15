from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.get("/")
def get_countries():
    return {"message" : "Hello World"}


@app.post("/bhfl")
def post_request():
    if request.is_json:
        odd, even = [], []
        data = request.get_json()
        _numbers = data['numbers']
        _num_list = []
        success = True
        for i in _numbers:
            if str(i).isdigit() or i == ',' or i == '[' or i == ']':
                if str(i).isdigit():
                    _num_list.append(int(i))
            else:
                success = False
                break

        if success is False:
            return {"is_success": "false", "user_id": "john_doe_17091999"}
        for i in _num_list:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return {"is_success": "true", "user_id": "john_doe_17091999", "odd": json.dumps(odd), "even": json.dumps(even)}, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True)
