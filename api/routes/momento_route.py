from flask import Blueprint

from api.controllers.momento_controller import inserir, listar

momento_bp = Blueprint("momentos", __name__)

momento_bp.post("/")(inserir)
momento_bp.get("/")(listar)