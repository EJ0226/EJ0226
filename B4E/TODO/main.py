from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.todo import router as todo
from router.user import router as user
from router.share import router as share

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo)
app.include_router(share)
app.include_router(user)