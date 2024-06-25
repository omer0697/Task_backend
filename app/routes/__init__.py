from flask import Blueprint

main_bp = Blueprint('main', __name__)

from . import user_routes, post_routes, comment_routes, album_routes, photo_routes, todo_routes
