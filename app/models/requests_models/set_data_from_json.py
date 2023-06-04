from pydantic import BaseModel


class SetDataFromJSONRequest(BaseModel):
    full_path: str = "path_to_file"
    encoding: str = "utf-8"
