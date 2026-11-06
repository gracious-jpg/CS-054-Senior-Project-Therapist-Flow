from app.database import get_connection


def create_therapist(name, email):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "INSERT INTO therapists (name, email) VALUES (?, ?)",
            (name, email)
        )
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()


def get_therapist(therapist_id):
    connection = get_connection()
    try:
        row = connection.execute(
            "SELECT * FROM therapists WHERE id = ?",
            (therapist_id,)
        ).fetchone()
        return dict(row) if row else None
    finally:
        connection.close()


def update_therapist(therapist_id, name, email):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "UPDATE therapists SET name = ?, email = ? WHERE id = ?",
            (name, email, therapist_id)
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()


def delete_therapist(therapist_id):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "DELETE FROM therapists WHERE id = ?",
            (therapist_id,)
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()


def create_schedule(therapist_id, date, start_time, end_time):
    connection = get_connection()
    try:
        cursor = connection.execute(
            """INSERT INTO schedules
               (therapist_id, date, start_time, end_time)
               VALUES (?, ?, ?, ?)""",
            (therapist_id, date, start_time, end_time)
        )
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()



def get_schedule(schedule_id):
    connection = get_connection()
    try:
        row = connection.execute(
            "SELECT * FROM schedules WHERE id = ?",
            (schedule_id,)
        ).fetchone()
        return dict(row) if row else None
    finally:
        connection.close()



def update_schedule(schedule_id, date, start_time, end_time):
    connection = get_connection()
    try:
        cursor = connection.execute(
            """UPDATE schedules
               SET date = ?, start_time = ?, end_time = ?
               WHERE id = ?""",
            (date, start_time, end_time, schedule_id)
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()



def delete_schedule(schedule_id):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "DELETE FROM schedules WHERE id = ?",
            (schedule_id,)
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()


def create_session(therapist_id, session_date, duration):
    connection = get_connection()
    try:
        cursor = connection.execute(
            """INSERT INTO sessions (therapist_id, session_date, duration)
            VALUES (?, ?, ?)""",
            (therapist_id, session_date, duration)
        )
        connection.commit()
        return cursor.lastrowid
    finally:
        connection.close()


def get_session(session_id):
    connection = get_connection()
    try:
        row = connection.execute(
            "SELECT * FROM sessions WHERE id = ?",
            (session_id,)
        ).fetchone()
        return dict(row) if row else None
    finally:
        connection.close()


def update_session(session_id, session_date, duration):
    connection = get_connection()
    try:
        cursor = connection.execute(
            """UPDATE sessions
               SET session_date = ?, duration = ?
               WHERE id = ?""",
            (session_date, duration, session_id)
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()


def delete_session(session_id):
    connection = get_connection()
    try:
        cursor = connection.execute(
            "DELETE FROM sessions WHERE id = ?",
            (session_id,)
        )
        connection.commit()
        return cursor.rowcount > 0
    finally:
        connection.close()