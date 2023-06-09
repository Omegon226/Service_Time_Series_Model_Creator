from pydantic import BaseModel


class SetDataFromJSONBytesRequest(BaseModel):
    bytestring: bytes
    encoding: str = "utf-8"
