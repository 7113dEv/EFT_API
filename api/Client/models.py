import requests


class BaseClient():
    def __init__(self) -> None:
        self.url = settings.API_URL,
        self.retry = 0

    def post(self, request_query: str):
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(self.url, headers=headers, json={"query": request_query})
            response.raise_for_status()
        except requests.exceptions.HTTPError as req_err:
             print(f"Request exception occurred. Error: {req_err.response}. Args: {req_err.args}")
            # TODO: Exponential backoff strat

        return response.json()

            

             