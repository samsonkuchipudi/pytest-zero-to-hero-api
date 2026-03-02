import pytest

pytestmark = [pytest.mark.api]


def test_get_posts(api_client):
    response = api_client.get_posts()

    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) > 0

    first_post = posts[0]
    assert "id" in first_post
    assert "title" in first_post
    assert "body" in first_post


@pytest.mark.parametrize("post_id", [1, 5, 10, 50])
def test_get_post_by_valid_id(api_client, post_id):
    response = api_client.get_post_by_id(post_id)

    assert response.status_code == 200

    post = response.json()
    assert post["id"] == post_id
    assert "title" in post
    assert "body" in post


def test_get_post_by_invalid_id(api_client):
    # For JSONPlaceholder, invalid ID returns an empty object {} with 404 in many cases.
    response = api_client.get_post_by_id(9999)

    # Some public APIs may return 404, others 200 with empty body.
    # JSONPlaceholder typically returns 404 for non-existing resource.
    assert response.status_code == 404


def test_create_post(api_client):
    payload = {
        "title": "Samson Day 2",
        "body": "Learning pytest API framework",
        "userId": 1
    }

    response = api_client.create_post(payload)

    assert response.status_code == 201

    created = response.json()
    assert created["title"] == payload["title"]
    assert created["body"] == payload["body"]
    assert created["userId"] == payload["userId"]
    assert "id" in created