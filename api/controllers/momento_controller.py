from datetime import datetime
from flask import jsonify, request

from api.dtos.default_generic_response_dto import DefaultGenericResponseDto
from api.dtos.momento.filtro_momento_dto import FiltroMomentoDto
from api.models.momento import Momento
from api.schemas.momento_schema import MomentoInputSchema

momento_list = []


def inserir():
    """
    Insere um novo momento.
    ---
    tags:
      - Momentos

    consumes:
      - application/json

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - descricao
            - timestamp
            - latitude
            - longitude
          properties:
            descricao:
              type: string
              example: "Fiz meus primeiros 10km."

            timestamp:
              type: string
              format: date-time
              example: "2026-07-07T20:48:00-03:00"

            latitude:
              type: number
              format: double
              example: -10.689931630776984

            longitude:
              type: number
              format: double
              example: -37.42178240832807

    responses:
      201:
        description: Momento inserido com sucesso.

      400:
        description: Requisição inválida.
    """
    dados = request.get_json()

    dados_validados = MomentoInputSchema().load(dados)

    momento = Momento(
        id=len(momento_list) + 1,
        descricao=dados_validados.get("descricao"),
        timestamp=dados_validados.get("timestamp"),
        latitude=dados_validados.get("latitude"),
        longitude=dados_validados.get("longitude"),
    )

    momento_list.append(momento)

    response = DefaultGenericResponseDto(
        success=True,
        message="Momento inserido com sucesso.",
        data=momento.to_dict(),
    )

    return jsonify(response.to_dict()), 201


def listar():
    """
    Lista todos os momentos.
    ---
    tags:
      - Momentos
    parameters:
      - name: ultimo
        in: query
        type: boolean
        required: false
        description: Se true, retorna apenas o último momento inserido.
    responses:
      200:
        description: Lista de momentos
    """

    filtros = FiltroMomentoDto().load(request.args)

    momentos_dict = [momento.to_dict() for momento in momento_list]

    if filtros["ultimo"] and momentos_dict:
        momentos_dict = [momentos_dict[-1]]

    response = DefaultGenericResponseDto(
        success=True,
        message="Lista de momentos encontradas com sucesso.",
        data=momentos_dict,
    )

    return jsonify(response.to_dict()), 200
