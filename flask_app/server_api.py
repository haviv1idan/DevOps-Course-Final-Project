from logging import basicConfig, getLogger, DEBUG
from requests import get
from curlify import to_curl
from json import dumps

logging_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
basicConfig(level=DEBUG)


class API:

    def __init__(self, url: str = None):
        self.url = url or "http://python_server:8000"
        self.logger = getLogger("API")

    def get_questions(self, num: int = 0) -> list[dict]:
        url = f"{self.url}/questions/"
        self.logger.info(f"Sending GET request to {url}")

        if not num:
            response = get(url)
        else:
            response = get(url, params={"num": num})

        self.logger.info(to_curl(response.request))
        response = response.json()
        self.logger.info(f"Response: {dumps(response, indent=4)}")
        return response
