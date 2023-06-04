from pydantic import BaseModel


class SetDataFromCSVFileRequest(BaseModel):
    sep: str = ";"
    decimal: str = ","
    encoding: str = "utf-8"

