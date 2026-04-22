import requests

from utils import GREEN, RED, RESET, SERVER_API, checkRespOk, deco, decoTitle

USERNAME = "USERNAME"
EMAIL = "EMAIL"
PASSWORD = "PASSWORD"

@deco
def signup():
    resp = requests.post(SERVER_API+"/signup", json={
        "username": USERNAME,
        "email": EMAIL,
        "password": PASSWORD,
    })
    checkRespOk(resp, "Signup1", 201)
    resp = requests.post(SERVER_API+"/signup", json={
        "username": USERNAME,
        "email": EMAIL,
        "password": PASSWORD,
    })
    if resp.status_code != 409 or resp.json()["message"] != "username is already taken":
        print(f"{RED}failed test 'Signup2': {resp.status_code} {resp.content}{RESET}")
    else:
        print(f"{GREEN}Signup2: test passed{RESET}")

@deco
def login():
    # success
    resp = requests.post(SERVER_API+"/login", json={
        "username": USERNAME,
        "email": EMAIL,
        "password": PASSWORD,
    })
    if resp.status_code == 201:
        sessionToken = resp.cookies.get("sessionToken")
        if sessionToken:
            checkRespOk(resp, "Login1", 201)
        else:
            checkRespOk(resp, "Login1", -1)
    # error wrong username
    resp = requests.post(SERVER_API+"/login", json={
        "username": "Wrong",
        "email": EMAIL,
        "password": PASSWORD,
    })
    if resp.status_code == 201:
        sessionToken = resp.cookies.get("sessionToken")
        if sessionToken:
            checkRespOk(resp, "Login2", 201)
        else:
            checkRespOk(resp, "Login2", -1)

@decoTitle
def auth():
    signup()
    login()

if __name__ == "__main__":
    auth()

