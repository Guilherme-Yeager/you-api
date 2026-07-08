from marshmallow import Schema, fields


class FiltroMomentoDto(Schema):

    ultimo = fields.Boolean(load_default=False)
