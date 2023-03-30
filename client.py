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
req = requests.post("http://127.0.0.1:5000/bookings", data=json.dumps(data))
print(req.json())