from pydantic import BaseModel, StrictStr


class ShortenResponse(BaseModel):
    result_url: StrictStr


class ImageInfo(BaseModel):
    message: StrictStr
    status: StrictStr

class ErrorResponse(BaseModel):
    error: StrictStr