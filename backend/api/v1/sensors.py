from flask_restx import Namespace, Resource, fields
from flask import request
from api.v1.schemas import SensorReadingSchema
from api import api

# Создаём namespace для датчиков
ns = Namespace('sensors', description='Операции с датчиками')

# Модель для документации в Swagger
reading_model = ns.model('Reading', {
    'sensor_id': fields.String(required=True, min_length=36, description='UUID датчика'),
    'value': fields.Float(required=True, description='Значение измерения'),
    'timestamp': fields.DateTime(required=True, description='Время измерения (ISO)'),
    'location': fields.Nested(ns.model('Location', {
        'lat': fields.Float(required=True),
        'lon': fields.Float(required=True)
    }), required=True, description='Геолокация')
})

@ns.route('/readings')
class Readings(Resource):
    @ns.expect(reading_model)
    @ns.response(201, 'Успешно добавлено')
    @ns.response(400, 'Ошибка валидации')
    def post(self):
        """Добавить новое измерение"""
        schema = SensorReadingSchema()
        errors = schema.validate(request.json)
        if errors:
            return {"errors": errors}, 400
        
        return {"status": "success", "data": request.json}, 201

@ns.route('/test')
class Test(Resource):
    def get(self):
        """Тестовый эндпоинт для проверки"""
        return {"message": "sensors blueprint works"}