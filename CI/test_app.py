import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_addition(client):
    response = client.get("/calculate?num1=10&num2=5&operation=add")
    assert response.status_code == 200
    assert response.get_json()["result"] == 15


def test_subtraction(client):
    response = client.get("/calculate?num1=10&num2=5&operation=sub")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_multiplication(client):
    response = client.get("/calculate?num1=10&num2=5&operation=mul")
    assert response.status_code == 200
    assert response.get_json()["result"] == 50


def test_division(client):
    response = client.get("/calculate?num1=10&num2=2&operation=div")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5.0


def test_division_by_zero(client):
    response = client.get("/calculate?num1=10&num2=0&operation=div")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_invalid_operation(client):
    response = client.get("/calculate?num1=10&num2=5&operation=mod")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_invalid_input(client):
    response = client.get("/calculate?num1=ten&num2=5&operation=add")
    assert response.status_code == 400
    assert "error" in response.get_json()