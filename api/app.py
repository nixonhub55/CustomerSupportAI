from fastapi import FastAPI
from api.routes import router
from framework.kernel import Kernel

app.include_router(router)

app = FastAPI(
    title="Customer Support AI",
    version="1.0.0"
)

kernel = Kernel()

kernel.boot()