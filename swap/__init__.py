import logging
import json
import requests
import azure.functions as func

spotify_client_id = None
spotify_client_secret = None
spotify_token_endpoint = "https://accounts.spotify.com/api/token"


def main(request: func.HttpRequest) -> func.HttpResponse:
    request_json = request.get_json()
    # TODO: Add Spotify Client ID and Secret to request.
    return requests.post(spotify_token_endpoint, request_json)
