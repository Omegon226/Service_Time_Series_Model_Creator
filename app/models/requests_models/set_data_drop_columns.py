from pydantic import BaseModel
from typing import Union, List


class SetDataDropColumns(BaseModel):
    columns_to_drop: Union[str, List[str]] = "07LAB50CF001"
