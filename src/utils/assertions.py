def assert_user_structure(user: dict):
    assert "id" in user
    assert "name" in user
    assert "email" in user

    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)

    assert user["name"] != ""
    assert user["email"] != ""