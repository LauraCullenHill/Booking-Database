import mysql.connector


class DBConnectionError(Exception):
    pass


def get_mysql_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="LauraCullen",
        password="Hector2021-",
        auth_plugin='mysql_native_password',
        database="nano")


def get_all_availabilities_for_day(day):
    conn = None  # Initialize conn as None to close it later if needed
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor(dictionary=True)
        # %s is a placeholder for the parameters
        query = "select teamMember, `12-13`, `13-14`, `14-15`, `15-16`, `16-17`, `17-18`" \
                + "from salon_bookings where bookingDate = %s"
        # (day,) here is a tuple of the parameter values
        cursor.execute(query, (day,))
        result = cursor.fetchall()
        cursor.close()
        return result
    except Exception as exc:
        # from exc gives context
        raise DBConnectionError("Failed to get all availabilities for a stylist") from exc
    finally:
        if conn:
            conn.close()


stylists = get_all_availabilities_for_day("20230105")
for stylist in stylists:
    print(f"{stylist['teamMember']} at 5pm: {stylist['17-18']}")