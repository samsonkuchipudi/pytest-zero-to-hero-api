from src.api.clients.jsonplaceholder_client import JsonPlaceholderClient

# def test_list_users(base_url):
#     #triggering api and saving the response directly 
#     # response = requests.get(f"{base_url}/posts/1")
#     #Validating the status code of Get request.

#     client = JsonPlaceholderClient(base_url)
#     response = client.list_users(1)
#     assert response.status_code == 200

#     body = response.json()
#     print(body)


#     #All test validations of API
#     # assert "userId" in body
#     # assert body["userId"] == 1
#     # assert "id" in body
#     # assert body["id"] == 1
#     # assert "title" in body
#     # assert body["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    