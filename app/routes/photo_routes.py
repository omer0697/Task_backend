from flask import jsonify, request, abort
from app import db
from app.models.photo import Photo
from app.models.album import Album
from app.routes import main_bp

@main_bp.route('/photos', methods=['GET'])
def get_photos():
    photos = Photo.query.all()
    return jsonify([photo.serialize for photo in photos])

@main_bp.route('/photos/<int:id>', methods=['GET'])
def get_photo(id):
    photo = Photo.query.get_or_404(id)
    return jsonify(photo.serialize)

@main_bp.route('/photos', methods=['POST'])
def create_photo():
    data = request.get_json()
    
    # Check if the album exists
    album = Album.query.get(data['album_id'])
    if not album:
        return jsonify({"error": "Album not found"}), 404

    new_photo = Photo(**data)
    
    db.session.add(new_photo)
    db.session.commit()
    
    return jsonify(new_photo.serialize), 201

@main_bp.route('/photos/<int:id>', methods=['PUT'])
def update_photo(id):
    photo = Photo.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(photo, key, value)
    db.session.commit()
    return jsonify(photo.serialize)

@main_bp.route('/photos/<int:id>', methods=['DELETE'])
def delete_photo(id):
    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    return '', 204
