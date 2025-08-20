from flask import Flask, jsonify
app = Flask(__name__)
1
@app.route("/")
def index():
return jsonify({"message": "Funcionaaa"}) # change for something unique
if __name__ == "__main__":
app.run(threaded=True, host='0.0.0.0', port=3000)
