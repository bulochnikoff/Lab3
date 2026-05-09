from flask import Blueprint, jsonify, request
from api.v1.schemas import SensorReadingSchema

bp = Blueprint('sensors', __name__, url_prefix='/api/v1/sensors')


@bp.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "sensors blueprint works"})

# Новый POST для добавления показаний
@bp.route('/readings', methods=['POST'])
def add_reading():
    schema = SensorReadingSchema()
    # Валидируем входящие данные
    errors = schema.validate(request.json)
    if errors:
        return jsonify({"errors": errors}), 400

    

    return jsonify({
        "status": "success",
        "data": request.json
    }), 201