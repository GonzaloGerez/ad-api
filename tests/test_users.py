def test_get_user_balance(client):
    response= client.get("api/users/1/balance")
    assert response.status_code == 200
    assert response.json() == {"balance": 250000}

def test_create_user(client):
    user_data = {"name": "New User", "email": "new@example.com", "balance": 24000}
    response = client.post("api/users", json= user_data)
    assert response.status_code == 200
    assert response.json()["name"]== "New User"