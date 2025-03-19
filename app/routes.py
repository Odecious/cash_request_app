from flask import Blueprint, jsonify

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def home():
    return jsonify({"message": "Welcome to the Cash Request App!"})

@routes_bp.route('/home')
def homepage():
    return jsonify({"message": "This is the Home Page!"})

