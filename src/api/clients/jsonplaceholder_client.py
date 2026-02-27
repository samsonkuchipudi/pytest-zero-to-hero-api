# import requests

# class Jsonplaceholderclient:

#     def __init__(self, base_url):
#         self.base_url = base_url

#     def list_users(self, userId):
#         return requests.get(f"{self.base_url}/posts", params={"userId": userId})

import requests


class JsonPlaceholderClient:
    """
    A small API client that knows HOW to talk to JSONPlaceholder.

    Tests will call methods like:
        api_client.get_users()
        api_client.get_post_by_id(1)

    The client will handle:
    - building URLs
    - using a shared HTTP session
    """

    def __init__(self, base_url: str):
        # Example base_url: "https://jsonplaceholder.typicode.com"
        # rstrip("/") removes a trailing slash if present.
        # "https://x.com/" becomes "https://x.com"
        self.base_url = base_url.rstrip("/")

        # requests.Session() keeps a reusable connection under the hood.
        # It's faster and allows common headers/auth later.
        self.session = requests.Session()

    def get_users(self):
        """
        GET /users
        Returns the requests.Response object
        """
        url = f"{self.base_url}/users"
        return self.session.get(url, timeout=10)

    def get_posts(self):
        """
        GET /posts
        """
        url = f"{self.base_url}/posts"
        return self.session.get(url, timeout=10)

    def get_post_by_id(self, post_id: int):
        """
        GET /posts/{id}
        """
        url = f"{self.base_url}/posts/{post_id}"
        return self.session.get(url, timeout=10)

    def create_post(self, payload: dict):
        """
        POST /posts
        payload is sent as JSON body
        """
        url = f"{self.base_url}/posts"
        return self.session.post(url, json=payload, timeout=10)