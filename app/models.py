import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            link TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending'
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, link):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO tasks (link) VALUES (?)", (link,))
        self.conn.commit()
        # Returns the created id using lastrowid.
        return cur.lastrowid

    def remove_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = ?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def get_pending_tasks(self):
        query = "SELECT * FROM tasks WHERE status = 'pending'"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def close(self):
        self.conn.close()