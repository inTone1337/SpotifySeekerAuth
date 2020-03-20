import logging

import azure.functions as func

spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(req: func.HttpRequest) -> func.HttpResponse:
    json = req.get_json()
    grant_type = json["grant_type"]
    code = json["code"]
    redirect_uri = json["redirect_uri"]
    return func.HttpResponse(f"Received {json}.")

# TODO: Add separate routing and logic for /swap and /refresh endpoints.
def refresh(req: func.HttpRequest) -> func.HttpResponse:
    return None