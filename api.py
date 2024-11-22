from flask import Flask, request, jsonify
from database import Database  # Импортируем db из database.py

app = Flask(__name__)

@app.route('/stats', methods=['POST'])
def add_stats():
    db = Database()
    data = request.json
    score = data.get('score')

    if score is None:
        return jsonify({'error': 'Score is missing'}), 400

    try:
        db.add_stats(score)
        return jsonify({'message': 'Score added successfully'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")  # Логирование ошибки
        return jsonify({'error': 'Failed to add score'}), 500

if __name__ == '__main__':
    app.run(debug=True)