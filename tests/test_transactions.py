def test_create_transaction(client):
    transaction_data= {"from_user_id": 1, "to_user_id": 2, "amount": 2500}
    response = client.post("api/transactions", json= transaction_data)
    assert response.status_code == 200
    assert response.json()["id"] == 1