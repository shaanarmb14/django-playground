from ninja import Schema

class NotFoundError(Schema):
    detail: str