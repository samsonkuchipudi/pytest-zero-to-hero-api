import pytest
from src.utils.assertions import assert_user_structure

pytestmark = [pytest.mark.api]


def test_get_users(api_client):
    response = api_client.get_users()

    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    assert_user_structure(users[0])

    # # Check a few expected fields in first item
    # first_user = users[0]
    # # assert "id" in first_user
    # # assert "name" in first_user
    # # assert "email" in first_user
    # assert isinstance(first_user["id"], int)
    # assert isinstance(first_user["email"], str)
    # assert first_user["email"] != ""
    # assert response.elapsed.total_seconds() < 2