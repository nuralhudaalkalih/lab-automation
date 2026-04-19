import sqlite3
class DatabaseManager:
    def __init__(self, db_path="lab.db"):
        self.db_path = db_path
        self.connection= sqlite3.connect(self.db_path)
        self.connection.row_factory=sqlite3.Row #ACCESS TO COLUMNS BY NAME instead of index
        self.cursor=self.connection.cursor() #execute sql commands
        self.create_tables()
    def create_tables(self):
        # executescript allows us to execute multiple SQL statements at once
       self.cursor.executescript("""
            -- 'role' is constrained to only two valid strings.
            CREATE TABLE IF NOT EXISTS Users (
                user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
                username  TEXT    NOT NULL UNIQUE,
                password  TEXT    NOT NULL,
                role      TEXT    NOT NULL CHECK(role IN ('Admin', 'Technician'))
            );

            -- One row per patient sample received by the lab.
            -- sample_id is set manually (e.g. "S001") instead of AUTOINCREMENT for convetion
            CREATE TABLE IF NOT EXISTS Samples (
                sample_id    TEXT PRIMARY KEY,
                patient_name TEXT NOT NULL,
                date_added   TEXT NOT NULL,
                status       TEXT NOT NULL DEFAULT 'Pending'
                             CHECK(status IN ('Pending','Processing','Completed'))
            );
 
            
            -- A catalogue of all test types the lab can perform.
            -- example: CBC, Urinalysis, COVID-19 PCR, TSH
            CREATE TABLE IF NOT EXISTS Tests (
                test_id     INTEGER PRIMARY KEY AUTOINCREMENT,
                test_name   TEXT    NOT NULL UNIQUE,
                description TEXT
            );

            -- Links a Sample to a Test and stores the measured value.
            -- One sample can have many results (one per test performed on it).
                CREATE TABLE IF NOT EXISTS Results (
                result_id    INTEGER PRIMARY KEY AUTOINCREMENT,
                sample_id    TEXT    NOT NULL,
                test_id      INTEGER NOT NULL,
                result_value TEXT,
                FOREIGN KEY (sample_id) REFERENCES Samples(sample_id)
                    ON DELETE CASCADE,
                FOREIGN KEY (test_id)   REFERENCES Tests(test_id)
                    ON DELETE RESTRICT
            );
        """)
        self.conn.commit()
 

    def close(self):
        self.connection.close()