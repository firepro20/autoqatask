import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def get_booking(booking_id):
    response = requests.get(f"{BASE_URL}/booking/{booking_id}")
    return response