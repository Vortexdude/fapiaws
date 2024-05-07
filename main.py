from typing import Any, Optional

from fastapi import FastAPI, Depends
from pydantic_settings import BaseSettings
from fastapi_cognito import CognitoAuth, CognitoSettings, CognitoToken

app = FastAPI()


class Settings(BaseSettings):
    check_expiration: bool = True
    jwt_header_prefix: str = "Bearer"
    jwt_header_name: str = "Authorization"
    userpools: dict[str, dict[str, Any]] = {
        "us": {
            "region": "us-east-1",
            "userpool_id": "us-east-1_BfjnUKzQx",
            "app_client_id": "5c4t4609stj5feai9bqdfqdjr1"
        }
    }


settings = Settings()

cognito_us = CognitoAuth(
    settings=CognitoSettings.from_global_settings(settings),
    userpool_name="us"
)


class CustomTokenModel(CognitoToken):
    custom_value: Optional[str] = None


cognito = CognitoAuth(
    settings=CognitoSettings.from_global_settings(settings),
    # Here we provide custom token model
    custom_model=CustomTokenModel
)

@app.get("/")
def hello_world(auth: CustomTokenModel = Depends(cognito.auth_required)):
    return {"message": f"Hello {auth.custom_value}"}

# @app.get("/")
# def hello_world(auth: CognitoToken = Depends(cognito_us.auth_required)):
#     return {"message": "Hello world"}



