from flask import jsonify
from marshmallow import ValidationError

from api.dtos.default_generic_response_dto import DefaultGenericResponseDto


def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(error):
        response = DefaultGenericResponseDto(
            success=False,
            message="Erro de validação nos campos enviados.",
            data=error.messages,
        )
        return jsonify(response.to_dict()), 400

    @app.errorhandler(Exception)
    def handle_exception(error):

        response = DefaultGenericResponseDto(
            success=False,
            message="Erro interno do servidor.",
            data=None,
        )

        return jsonify(response.to_dict()), 500
