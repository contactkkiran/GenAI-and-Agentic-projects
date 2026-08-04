from pydantic import BaseModel

from fastapi import FastAPI

# Swagger UI: http://
api = FastAPI()


# Get Request
@api.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


@api.get("/welcome")
def welcome():
    return {"message": "Hello Kiran"}


@api.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}"}


@api.get("/address/{name}")
def adddress(name: str):
    return {
        "message": f"Hello {name}",
        "address": "123 Main St, City, Country",
    }


# Post Request


class User(BaseModel):
    name: str
    city: str
    age: int


@api.post("/createuser")
def create_user(user: User):
    return {
        "message": f"User {user.name} from {user.city} aged {user.age} created successfully."
    }


class RegisterUser(BaseModel):
    name: str
    email: str
    password: str


@api.post("/register")
def register_user(user: RegisterUser):
    return {
        "message": f"User {user.name} with  {user.email} registered successfully./n ",
        "status": "successfully registered",
    }


# 🟢 Next Step: Async Endpoints with FastAPI (using asyncio)
# Concept in Simple Words
# Normally, Python runs one request at a time.

# With async, Python can handle multiple requests simultaneously without waiting
#  for one to finish before starting another.

# Example: If one request is waiting for a database, another request
#  can still be processed.

# Why Async Is Used in Real Projects
# Performance → Handle thousands of requests per second.
# Non-blocking I/O → Don’t freeze while waiting for external services (DB, APIs).
# Scalability → Essential for microservices, chat apps, and real-time dashboards.

import asyncio

api = FastAPI()


@api.get("/wait/{seconds}")
async def slow_endpoint(seconds: str):
    await asyncio.sleep(int(seconds))  # Simulate a slow operation
    return {"message": "This is a slow endpoint"}
