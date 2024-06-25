from flask import jsonify, request, abort
from app import db
from app.models.user import User, Address, Geo, Company
from app.routes import main_bp

@main_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize for user in users])

@main_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id) # Returns 404 if not found in database
    return jsonify(user.serialize)

@main_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Check if username already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists"}), 400

    # Create nested objects
    address_data = data.pop('address')
    geo_data = address_data.pop('geo')
    company_data = data.pop('company')
    
    geo = Geo(**geo_data) #  ** unpacks the dictionary => Geo(lat=geo_data['lat'], lng=geo_data['lng'])
    address = Address(**address_data, geo=geo) # Address(street=address_data['street'], suite=address_data['suite'], city=address_data['city'], zipcode=address_data['zipcode'], geo=geo)
    company = Company(**company_data)
    
    new_user = User(**data, address=address, company=company)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.serialize), 201

@main_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return jsonify(user.serialize)

@main_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

@main_bp.route('/all_users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.serialize for user in users])
