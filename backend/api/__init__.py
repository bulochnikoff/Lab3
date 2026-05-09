from flask_restx import Api

api = Api(
    version='1.0',
    title='Research Dashboard API',
    description='API для интеграции научных данных',
    doc='/api/docs/'
)

# Импортируем namespace из sensors и регистрируем его
from api.v1.sensors import ns as sensors_ns
api.add_namespace(sensors_ns, path='/api/v1')