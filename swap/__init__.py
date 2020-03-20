import logging

import azure.functions as func

spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(req: func.HttpRequest) -> func.HttpResponse:
    json = req.get_json()
    grant_type = json["grant_type"]
    code = json["code"]
    redirect_uri = json["redirect_uri"]
    return func.HttpResponse(f"Received {json}.")

# TODO: Figure out how to get separate routing for /swap and /refresh.
def refresh(req: func.HttpRequest) -> func.HttpResponse:
    json = req.get_json()
    grant_type = json["grant_type"]
    refresh_token = json["refresh_token"]
    return func.HttpResponse(f"Received {json}.")