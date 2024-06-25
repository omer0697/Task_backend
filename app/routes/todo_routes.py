from flask import jsonify, request, abort
from app import db
from app.models.todo import Todo
from app.models.user import User
from app.routes import main_bp

@main_bp.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([todo.serialize for todo in todos])

@main_bp.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return jsonify(todo.serialize)

@main_bp.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    
    # Check if the user exists
    user = User.query.get(data['user_id'])
    if not user:
        return jsonify({"error": "User not found"}), 404

    new_todo = Todo(**data)
    
    db.session.add(new_todo)
    db.session.commit()
    
    return jsonify(new_todo.serialize), 201

@main_bp.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(todo, key, value)
    db.session.commit()
    return jsonify(todo.serialize)

@main_bp.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204
