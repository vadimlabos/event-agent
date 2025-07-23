from typing import Optional

from pydantic import BaseModel


class Event(BaseModel):
    session: Optional[list[dict[str,int]]] = None
