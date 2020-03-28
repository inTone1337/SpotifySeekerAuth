import logging
import json
import requests
import azure.functions as func

spotify_client_id = None
spotify_secret = None
spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(request: func.HttpRequest) -> func.HttpResponse:
    # TODO: Add Spotify Client ID and Secret to request.
    spotify_request = requests.post(spotify_token_endpoint, request.get_json())
    logging.debug(spotify_request.text)

    # TODO: Fill this with data received from Spotify.
    response = {}
    response["access_token"] = None
    response["expires_in"] = None
    response["refresh_token"] = None
    response_json = json.dumps(response)

    return func.HttpResponse(f"Received {request.get_json()}. Replied {response_json}.")