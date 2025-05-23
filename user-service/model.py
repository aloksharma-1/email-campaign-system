from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: str
    disabled: Optional[bool] = False

class UserInDB(User):
    hashed_password: str

fake_users_db = {
    "alok": {
        "username": "alok",
        "email": "alok@example.com",
        "hashed_password": "secret",
        "disabled": False,
    }
}

def get_user(username: str):
    user = fake_users_db.get(username)
    if user:
        return UserInDB(**user)
    return None
