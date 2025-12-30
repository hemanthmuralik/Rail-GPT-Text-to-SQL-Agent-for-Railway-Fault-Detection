import sqlite3
import random
from datetime import datetime, timedelta

# Connect
conn = sqlite3.connect('railway_production.db')
cursor = conn.cursor()

# Create Table
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

# Configuration
locations = ['Pune_Station', 'Lonavala_Ghat', 'Mumbai_Central', 'Thane_Junction', 'Kalyan_Yard']
faults = ['Crack', 'Misalignment', 'Obstacle', 'Signal_Failure', 'Corrosion']
statuses = ['Detected', 'Pending', 'In_Progress', 'Resolved']

# Generate 500 Rows
data = []
start_date = datetime(2025, 1, 1)

for i in range(1, 501):
    loc = random.choice(locations)
    # Random time in the last 365 days
    time_entry = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))
    f_type = random.choice(faults)
    # Higher confidence for detected, lower for others
    conf = round(random.uniform(0.75, 0.99), 2)
    stat = random.choice(statuses)
    
    data.append((i, loc, time_entry, f_type, conf, stat))

cursor.executemany('INSERT INTO faults VALUES (?, ?, ?, ?, ?, ?)', data)
conn.commit()
conn.close()
print(f"✅ Generated 'railway_production.db' with {len(data)} rows.")
