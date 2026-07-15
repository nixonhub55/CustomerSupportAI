from fastapi import APIRouter
from api.dependencies import kernel

router = APIRouter()


@router.post("/chat")
def chat(request: dict):

    answer = kernel.ask(
        request["message"]
    )

    return {
        "answer": answer
    }