# import pytest

# @pytest.fixture(scope="session")
# def base_url():
#     return "https://jsonplaceholder.typicode.com"

import pytest
from src.api.clients.jsonplaceholder_client import JsonPlaceholderClient


@pytest.fixture(scope="session")
def base_url():
    # Base URL is centralized here (easy to change later)
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_client(base_url):
    # Create ONE client for the entire test session
    return JsonPlaceholderClient(base_url)