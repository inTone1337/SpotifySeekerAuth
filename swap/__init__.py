import logging
import json
import azure.functions as func

spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(request: func.HttpRequest) -> func.HttpResponse:
    request_json = request.get_json()
    grant_type = request_json["grant_type"]
    code = request_json["code"]
    redirect_uri = request_json["redirect_uri"]

    # TODO: Fill this with data received from Spotify.
    response = {}
    response["access_token"] = None
    response["expires_in"] = None
    response["refresh_token"] = None
    response_json = json.dumps(response)

    return func.HttpResponse(f"Received {request_json}. Replied {response_json}.")
