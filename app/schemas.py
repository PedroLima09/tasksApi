from pydantic import BaseModel

class Message(BaseModel):
    phone: str
    message_type: str