from flask import Blueprint, jsonify

bp = Blueprint('sensors', __name__, url_prefix='/api/v1/sensors')

@bp.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "sensors blueprint works"})