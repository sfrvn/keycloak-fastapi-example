from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from keycloak import KeycloakOpenID


KEYCLOAK_URL = "http://127.0.0.1:8080"  # https://sso.aim.club
KEYCLOAK_REALM_NAME = "AimSsoRealm"
CLIENT_ID = "Datamall"
CLIENT_SECRET = "**********"

app = FastAPI()
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_URL,
    client_id=CLIENT_ID,
    realm_name=KEYCLOAK_REALM_NAME,
    client_secret_key=CLIENT_SECRET
)


@app.get("/auth/login")
async def login():
    auth_url = await keycloak_openid.a_auth_url(
        redirect_uri="http://localhost:8000/auth/callback",
        scope="email",
    )
    return RedirectResponse(auth_url)


@app.get("/auth/callback")
async def auth_callback(request: Request, code: str):
    access_token = await keycloak_openid.a_token(
        grant_type='authorization_code',
        code=code,
        redirect_uri="http://localhost:8000/auth/callback"
    )
    # TODO создать пользователя, сделать редирект на главную
    return {"access_token": access_token["access_token"]}
