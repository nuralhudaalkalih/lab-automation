class SampleDAO:
    def __init__(self, db_manager):
        self.db = db_manager

    def add_sample(self, sample_id, patient_name, date_added):
        self.db.cursor.execute(
            "INSERT INTO Samples VALUES (?, ?, ?, 'Pending')",
            (sample_id, patient_name, date_added)
        )
        self.db.conn.commit()

    def get_all_samples(self):
        self.db.cursor.execute("SELECT * FROM Samples")
        return self.db.cursor.fetchall()

    def update_status(self, sample_id, new_status):
        self.db.cursor.execute(
            "UPDATE Samples SET status = ? WHERE sample_id = ?",
            (new_status, sample_id)
        )
        self.db.conn.commit()

    def search_by_status(self, status):
        self.db.cursor.execute(
            "SELECT * FROM Samples WHERE status = ?", (status,)
        )
        return self.db.cursor.fetchall()