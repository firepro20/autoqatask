import pytest
from api_client import get_booking

def test_get_booking():
    booking_id = 1
    response = get_booking(booking_id)
    
    assert response.status_code == 200, "Booking retrieval failed!"
    assert "firstname" in response.json(), "Missing firstname in response"