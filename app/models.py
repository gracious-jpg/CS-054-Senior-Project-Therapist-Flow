from app.database import get_connection


def create_tables():
    connection = get_connection()

    try:
        connection.executescript("""
            CREATE TABLE IF NOT EXISTS therapists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS schedules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                therapist_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                FOREIGN KEY (therapist_id)
                    REFERENCES therapists(id)
            );

            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                therapist_id INTEGER NOT NULL,
                session_date TEXT NOT NULL,
                duration INTEGER NOT NULL,
                FOREIGN KEY (therapist_id)
                    REFERENCES therapists(id)
            );
        """)

        connection.commit()

    finally:
        connection.close()