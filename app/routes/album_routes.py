from flask import jsonify, request
from app import db
from app.models.album import Album
from app.routes import main_bp

@main_bp.route('/albums', methods=['GET'])
def get_albums():
    albums = Album.query.all()
    return jsonify([album.serialize for album in albums])

@main_bp.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    album = Album.query.get_or_404(id)
    return jsonify(album.serialize)

@main_bp.route('/albums', methods=['POST'])
def create_album():
    data = request.get_json()
    new_album = Album(**data)
    db.session.add(new_album)
    db.session.commit()
    return jsonify(new_album.serialize), 201

@main_bp.route('/albums/<int:id>', methods=['PUT'])
def update_album(id):
    album = Album.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(album, key, value)
    db.session.commit()
    return jsonify(album.serialize)

@main_bp.route('/albums/<int:id>', methods=['DELETE'])
def delete_album(id):
    album = Album.query.get_or_404(id)
    db.session.delete(album)
    db.session.commit()
    return '', 204
