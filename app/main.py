import re

from fastapi import FastAPI

from app.api.api import router as api_router

app = FastAPI()
app.include_router(api_router, prefix="/v1")


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Return True if email address is valid
def is_valid(email):
    # Regex for validating an Email
    regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    # Pass the regular expression
    # and the string in search() method
    if re.search(regex, email):
        return True
    else:
        return False
