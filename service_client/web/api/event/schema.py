from pydantic import BaseModel


class Event(BaseModel):
    """Simple message model."""

    event_type: str
    event_payload: str
