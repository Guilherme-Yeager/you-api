from flask import Flask
from flasgger import Swagger
from api.handler.handler import register_error_handlers
from api.swagger.swagger_config import swagger_template, swagger_config
from api.routes.momento_route import momento_bp

app = Flask(__name__)

Swagger(app, template=swagger_template, config=swagger_config)

register_error_handlers(app)

app.register_blueprint(momento_bp, url_prefix="/momentos")