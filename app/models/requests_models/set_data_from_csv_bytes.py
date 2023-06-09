from pydantic import BaseModel


class SetDataFromCSVBytesRequest(BaseModel):
    bytestring: bytes
    sep: str = ";"
    decimal: str = ","
    encoding: str = "utf-8"
