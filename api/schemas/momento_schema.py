from marshmallow import Schema, fields, validate


class MomentoInputSchema(Schema):

    descricao = fields.Str(
        required=True, error_messages={"required": "A descrição é obrigatória."}
    )

    timestamp = fields.DateTime(
        required=True,
        error_messages={
            "required": "O timestamp é obrigatório.",
            "invalid": "Formato de data inválido.",
        },
    )

    latitude = fields.Float(
        required=True,
        error_messages={
            "required": "A latitude é obrigatória.",
            "invalid": "A latitude deve ser um número válido.",
        },
    )
    longitude = fields.Float(
        required=True,
        error_messages={
            "required": "A longitude é obrigatória.",
            "invalid": "A longitude deve ser um número válido.",
        },
    )
