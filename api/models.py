from pydantic import BaseModel


class ChatRequest(BaseModel):

    assistant: str

    message: str


class ChatResponse(BaseModel):

    answer: str