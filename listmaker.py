import sqlite3
import json

# Connect to the SQLite database
conn = sqlite3.connect('HashDB')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a query to select all rows from the table
cursor.execute('SELECT * FROM HashDB')

# Fetch all rows from the cursor
rows = cursor.fetchall()

# Create an empty dictionary to store malware names and hashes
malware_dict = {}

# Iterate over the rows and populate the dictionary
for row in rows:
    hash_value = row[0]
    malware_name = row[1]
    if malware_name not in malware_dict:
        malware_dict[malware_name] = []
    malware_dict[malware_name].append(hash_value)

# Close the database connection
conn.close()

# Save the dictionary to a text file
with open('malware_hashes.txt', 'w') as file:
    json.dump(malware_dict, file, indent=4)

print("Malware names and hashes saved to 'malware_hashes.txt'")
