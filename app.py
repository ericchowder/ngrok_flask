from flask import Flask, request, jsonify

app = Flask(__name__)

# Health Test
@app.route('/')
def health():
    return "Good!"

# GET challenge route
@app.route('/challenge', methods=['GET'])
def get():
    if(request.args):
        challenge = request.args.get('challenge')
        return challenge
    else:
        return "No args"

# POST return body
@app.route('/return-body', methods=["POST"])
def post():
    body = request.data
    print(body)
    return jsonify(body.decode("utf-8"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)