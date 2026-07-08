from datetime import datetime


class Momento:

    def __init__(
        self,
        id: int | None,
        descricao: str,
        timestamp: datetime,
        latitude: float,
        longitude: float,
    ):
        self.id = id
        self.descricao = descricao
        self.ano = timestamp.year
        self.mes = timestamp.month
        self.dia = timestamp.day
        self.hora = timestamp.strftime("%H:%M:%S")
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "periodo": {
                "ano": self.ano,
                "mes": self.mes,
                "dia": self.dia,
                "hora": self.hora,
            },
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
