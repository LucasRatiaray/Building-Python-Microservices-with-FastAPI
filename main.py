from fastapi import FastAPI

app = FastAPI()

@app.get("/ch01/index")
def index():
    return {"message": "Welcome FastAPI Nerds"}

@app.get("/ch01/login")
def login(username: str, password: str):
    if valid_users.get(username) == None:
        return{"message": "user does not exit"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(),
                   user.passphrase.encode()):
            return user
        else:
            return {"message": "invalid user"}