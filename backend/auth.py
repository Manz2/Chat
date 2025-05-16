import jwt, time
from fastapi import HTTPException

SECRET = "secret"

users = {
    "malcom": {"username": "malcom", "password": "1234"},
    "kaylee": {"username": "kaylee", "password": "1234"},
}

def authenticate_user(username: str, password: str):
    user = users.get(username)
    if user and user["password"] == password:
        return user
    return None

def create_access_token(username: str):
    payload = {"sub": username, "exp": time.time() + 3600}
    return jwt.encode(payload, SECRET, algorithm="HS256")

def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {"username": payload["sub"]}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
