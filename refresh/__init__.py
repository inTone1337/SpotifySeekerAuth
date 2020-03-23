import logging

import azure.functions as func

spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(request: func.HttpRequest) -> func.HttpResponse:
    json = request.get_json()
    grant_type = json["grant_type"]
    refresh_token = json["refresh_token"]
    return func.HttpResponse(f"Received {json}.")