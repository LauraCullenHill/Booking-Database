from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, InternalServerError
from db import get_all_availabilities_for_day

app = Flask(__name__)


# URL to get all availabilities for a day
@app.route("/bookings", methods=["GET"])
def get_bookings():
    day = request.args.get("day", '')
    if not day:
        raise Exception("Please specify day")
    return jsonify(get_all_availabilities_for_day(day))

# URL to create a booking
@app.route("/bookings", methods=["GET"])
def add_bookings():
    try:
        data = request.json()
        db_add_booking(day, team_mate, time_slot, customer_name)
        return f'{data["customer_name"]} added booking for {data["team_mate"]} at {data["day"]} - {data["time_slot"]}'
    except Exception as exc:
        raise InternalServerError("Failed to load") from exc


if __name__ == '__main__':
    app.run(debug=True, port=5000)