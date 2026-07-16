from fastapi import APIRouter

from api.dependencies import kernel
from api.models import ChatRequest, ChatResponse

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    print("=" * 50)
    print("Assistant:", request.assistant)
    print("Message:", request.message)
    print("=" * 50)

    answer = kernel.ask(
        request.assistant,
        request.message
    )

    return ChatResponse(
        answer=answer
    )