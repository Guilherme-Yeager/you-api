from datetime import datetime
from flask import jsonify, request

from api.dto.default_generic_response import DefaultGenericResponse
from api.models.momento import Momento

momento_list = []


def inserir():
    dados = request.get_json()

    momento = Momento(
        id=None,
        descricao=dados.get("descricao"),
        timestamp=datetime.fromisoformat(dados["timestamp"]),
        latitude=dados.get("latitude"),
        longitude=dados.get("longitude"),
    )

    momento_list.append(momento)

    response = DefaultGenericResponse(
        success=True,
        message="Momento inserido com sucesso.",
        data=momento.to_dict(),
    )

    return jsonify(response.to_dict()), 201


def listar():
    momentos_dict = [momento.to_dict() for momento in momento_list]

    response = DefaultGenericResponse(
        success=True,
        message="Lista de momentos encontradas com sucesso.",
        data=momentos_dict,
    )

    return jsonify(response.to_dict()), 200
