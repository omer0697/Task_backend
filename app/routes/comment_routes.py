from flask import jsonify, request, abort
from app import db
from app.models.comment import Comment
from app.models.post import Post
from app.routes import main_bp

@main_bp.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.all()
    return jsonify([comment.serialize for comment in comments])

@main_bp.route('/comments/<int:id>', methods=['GET'])
def get_comment(id):
    comment = Comment.query.get_or_404(id)
    return jsonify(comment.serialize)

@main_bp.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    
    # Check if the post exists
    post = Post.query.get(data['post_id'])
    if not post:
        return jsonify({"error": "Post not found"}), 404

    new_comment = Comment(**data)
    
    db.session.add(new_comment)
    db.session.commit()
    
    return jsonify(new_comment.serialize), 201

@main_bp.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    comment = Comment.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(comment, key, value)
    db.session.commit()
    return jsonify(comment.serialize)

@main_bp.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    return '', 204
