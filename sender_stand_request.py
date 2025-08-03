import requests
import configuration
import data
import copy

def post_new_user():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers={"Content-Type": "application/json"}
    )

def get_new_user_token():
    response = post_new_user()
    return response.json()["authToken"]

def post_new_client_kit(kit_body, auth_token):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}"
        }
    )
