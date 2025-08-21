from flask import Flask, jsonify, request

app = Flask(__name__)
news = [{"id": 0, "title": ""
, "content": ""}]
next_id = 1  # simple auto-increment for IDs

@app.route("/", methods=["GET"])
def index():
    return jsonify({"hola": "todo funciona"}), 200

@app.route("/news", methods=["GET"])
def list_news():
    return jsonify({"count":len(news),"items": news})

@app.route("/news", methods=["POST"])
def create_news():
    data = request.json
    return jsonify(data), 201

@app.route("/news/<int:item_id>", methods=["PUT"])
def update_news(item_id: int):
    item = next((n for n in news if n["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    data = request.json
    for key in ("title", "content"):
        if key in data:
            item[key] = data[key]
    return jsonify(item)

@app.route("/news/<int:item_id>", methods=["DELETE"])
def delete_news(item_id: int):
    del news[item_id]
    return jsonify({"status": "deleted", "id": item_id})

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port=3001)
