import sqlite3

conn = sqlite3.connect('railway.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS faults (
    id INTEGER PRIMARY KEY,
    location TEXT,
    timestamp DATETIME,
    fault_type TEXT,
    confidence_score FLOAT,
    status TEXT
)
''')

# Insert Dummy Data
data = [
    (1, 'Pune', '2025-12-29 10:30:00', 'Crack', 0.92, 'Detected'),
    (2, 'Mumbai', '2025-12-29 11:15:00', 'Obstacle', 0.88, 'Resolved'),
    (3, 'Pune', '2025-12-29 14:00:00', 'Misalignment', 0.75, 'Pending'),
    (4, 'Lonavala', '2025-12-30 09:00:00', 'Crack', 0.95, 'Detected'),
    (5, 'Pune', '2025-12-30 09:45:00', 'Crack', 0.89, 'Detected')
]

cursor.executemany('INSERT INTO faults VALUES (?, ?, ?, ?, ?, ?)', data)
conn.commit()
conn.close()

print("✅ Database created!")