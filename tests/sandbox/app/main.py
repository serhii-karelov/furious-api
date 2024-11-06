from contextlib import asynccontextmanager
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app):
    print("Set up app")
    yield
    print("Tear down app")


app = FastAPI(title="Furious app", lifespan=lifespan)
