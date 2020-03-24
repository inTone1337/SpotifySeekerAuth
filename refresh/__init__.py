import logging
import json
import azure.functions as func

spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(request: func.HttpRequest) -> func.HttpResponse:
    request_json = request.get_json()
    grant_type = request_json["grant_type"]
    refresh_token = request_json["refresh_token"]

    # TODO: Fill this with data received from Spotify.
    response = {}
    response["access_token"] = None
    response["expires_in"] = None
    response_json = json.dumps(response)

    return func.HttpResponse(f"Received {request_json}. Replied {response_json}.")
