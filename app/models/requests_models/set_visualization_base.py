from pydantic import BaseModel
from typing import List, Union


class SetVisualizeBase(BaseModel):
    fig_weights: float = 15.
    fig_height: float = 5.
    params: Union[str, List[str]] | None = None
