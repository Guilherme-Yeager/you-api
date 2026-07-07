from flask import Flask

app = Flask(__name__)

from api.routes.momento_route import momento_bp

app.register_blueprint(momento_bp, url_prefix="/momentos")