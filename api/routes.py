from fastapi import APIRouter

from api.dependencies import kernel
from api.models import ChatRequest, ChatResponse

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    answer = kernel.ask(
        request.assistant,
        request.message
    )

    return ChatResponse(
        answer=answer
    )