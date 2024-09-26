from flask import Flask, jsonify, request

app = Flask(__name__)

# Global variable to store tasks
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]

# Route to return the list of todos (GET)
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Route to add a new task (POST)
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Convert request body to a Python dictionary
    request_body = request.get_json(force=True)
    # Append the new task to the list
    todos.append(request_body)
    # Return updated list of todos with 200 status code
    return jsonify(todos), 200

# Route to delete a task by position (DELETE)
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Check if the position is valid
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Position out of range"}), 400

    # Remove the todo at the specified position
    todos.pop(position)

    # Return the updated list of todos
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
