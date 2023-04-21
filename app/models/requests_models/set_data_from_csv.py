from pydantic import BaseModel


class SetDataFromCSVRequest(BaseModel):
    full_path: str = "ABOBA"
    sep: str = ";"
    decimal: str = ","
    encoding: str = "utf-8"
