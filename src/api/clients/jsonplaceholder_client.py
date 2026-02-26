import requests

class Jsonplaceholderclient:

    def __init__(self, base_url):
        self.base_url = base_url

    def list_users(self, userId):
        return requests.get(f"{self.base_url}/posts", params={"userId": userId})