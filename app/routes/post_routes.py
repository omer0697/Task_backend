from flask import jsonify, request
from app import db
from app.models.post import Post
from app.routes import main_bp

@main_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.serialize for post in posts])

@main_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.serialize)

@main_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(**data)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.serialize), 201

@main_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(post, key, value)
    db.session.commit()
    return jsonify(post.serialize)

@main_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return '', 204
