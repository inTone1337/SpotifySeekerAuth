import logging

import azure.functions as func

spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(request: func.HttpRequest) -> func.HttpResponse:
    json = request.get_json()
    grant_type = json["grant_type"]
    code = json["code"]
    redirect_uri = json["redirect_uri"]
    return func.HttpResponse(f"Received {json}.")