from flask import Flask, request, jsonfy

app = Flask(__name__)

tasks= []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'El campo "title" es obligatorio'}), 400

    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'done': False
    }
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
