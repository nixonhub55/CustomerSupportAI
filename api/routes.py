from fastapi import APIRouter

from api.app import kernel

router = APIRouter()


@router.post("/chat")
def chat(request: dict):

    question = request["message"]

    answer = kernel.ask(question)

    return {
        "answer": answer
    }