import requests
import json

# GET A BOOKING
# requests.get("http://127.0.0.1:5000/")
# print(req.content)


# post
data = {
    "day": "20230102",
    "team_mate": "anna",
    "time_slot": "12-13",
    "customer_name": "laura"
}
headers = {
    "content-type": "application/json"
}
req = requests.post("http://127.0.0.1:5000/bookings",
                    headers=headers,
                    data=json.dumps(data))
print(req.status_code)
print(req.content)

# CLIENT TODO:
# - add a nice panel that shows availabilities and allows bookings
# - interface for managing booking