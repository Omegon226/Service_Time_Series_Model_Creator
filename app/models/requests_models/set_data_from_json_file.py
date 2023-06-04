from pydantic import BaseModel


class SetDataFromJSONFileRequest(BaseModel):
    encoding: str = "utf-8"
