import pytest
from sqlmodel import SQLModel
from fastapi.testclient import TestClient
from hexagonal_arquitecture_example.main import app
from ..conftest import test_engine
from hexagonal_arquitecture_example.infrastructure.models.order_model import OrderModel


client = TestClient(app)


def test_integration_create_order_success():

    payload = {"product_id": 1, "quantity": 5, "customer_id": 3}

    response = client.post("orders/", json=payload)

    assert response.status_code == 201  # Assuming the ID is set to 1
    assert response.json()["product_id"] == 1
    assert response.json()["quantity"] == 5
    assert response.json()["customer_id"] == 3
