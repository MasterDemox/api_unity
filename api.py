from flask import Flask, request, jsonify
from database import Database
app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Hello World<p>"
@app.route("/stats")
def get_stats():
	db = Database()
	return db.get_stats()
@app.route("/allstats", methods=["GET", "POST"])
def add_stats():
	data = request.json
	if data is None:
		return jsonify({"error": "Invalid JSON"}), 400
	score = data.get('score')
	print(score)
	db = Database()
	db.add_stats(score)
	return jsonify({"status": "success", "received": data}), 200
if __name__ == "__main__":
	app.run(debug=True)