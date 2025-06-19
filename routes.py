from flask import Blueprint, request, jsonify
from app.model import get_recommendations

api = Blueprint('api', __name__)

@api.route('/recommend', methods=['GET'])
def recommend():
    try:
        item_id = int(request.args.get('id'))
        top_n = int(request.args.get('top', 3))
        results = get_recommendations(item_id, top_n)
        return jsonify({"recommendations": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
