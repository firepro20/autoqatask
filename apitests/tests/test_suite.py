import pytest
from api_client import *

@pytest.fixture(scope="module")
def auth_token():
    """Fixture to generate an authentication token"""
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=data)
    assert response.status_code == 200
    return response.json().get("token")


@pytest.fixture
def booking_id():
    """Fixture to create a booking and return its ID"""
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-03-01",
            "checkout": "2025-03-05"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=data)
    assert response.status_code == 200
    return response.json()["bookingid"]


def test_health_check():
    """Test to check if the API is up and running"""
    response = requests.get(f"{BASE_URL}/ping")
    assert response.status_code == 201


def test_get_booking(booking_id):
    """Test to retrieve a booking"""
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "John"
    assert response.json()["lastname"] == "Doe"


def test_update_booking(auth_token, booking_id):
    """Test to update a booking"""
    headers = {"Cookie": f"token={auth_token}", "Content-Type": "application/json"}
    data = {
        "firstname": "Jane",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-04-01",
            "checkout": "2025-04-10"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.put(f"{BASE_URL}/booking/{booking_id}", json=data, headers=headers)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Jane"
    assert response.json()["lastname"] == "Smith"


def test_delete_booking(auth_token, booking_id):
    """Test to delete a booking"""
    headers = {"Cookie": f"token={auth_token}"}
    response = requests.delete(f"{BASE_URL}/booking/{booking_id}", headers=headers)
    assert response.status_code == 201

