import sqlite3

DB_PATH = "Z:\\Projects\\FishDB\\Fish_info.sql"

def create_tables():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fish_data (
            id INTEGER PRIMARY KEY,
            common_name TEXT NOT NULL,
            scientific_name TEXT,
            max_size TEXT,
            remarks TEXT,
            min_tank_size TEXT,
            water_temp_range_f TEXT,
            pH_range TEXT,
            GH TEXT,
            KH TEXT,
            nitrate TEXT,
            dissolved_oxygen TEXT
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance_logs (
            id INTEGER PRIMARY KEY,
            timestamp TEXT NOT NULL,
            task_name TEXT NOT NULL,
            duration REAL NOT NULL,
            resources_used TEXT
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS error_logs (
            id INTEGER PRIMARY KEY,
            timestamp TEXT NOT NULL,
            error_message TEXT NOT NULL,
            line_number INTEGER,
            file_name TEXT
        );
        """)

def insert_data(data):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO fish_data (
            common_name, scientific_name, max_size, remarks, min_tank_size, 
            water_temp_range_f, pH_range, GH, KH, nitrate, dissolved_oxygen
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data['common_name'], data['scientific_name'], data['max_size'], data['remarks'], 
            data['min_tank_size'], data['water_temp_range_f'], data['pH_range'], 
            data['GH'], data['KH'], data['nitrate'], data['dissolved_oxygen']
        ))
        conn.commit()

if __name__ == "__main__":
    create_tables()
