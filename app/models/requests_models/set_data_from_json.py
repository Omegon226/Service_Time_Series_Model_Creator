from pydantic import BaseModel


class SetDataFromJSONRequest(BaseModel):
    full_path: str = "ABOBA"
    encoding: str = "utf-8"
