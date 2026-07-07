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
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            "id": self.id,
            "descricao": self.descricao,
            "timestamp": self.timestamp.isoformat(),
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
