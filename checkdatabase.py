import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("conversation_data.db")
cursor = conn.cursor()

# Fetch the names of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = cursor.fetchall()

# Print the table names
print("Available tables:")
for i, table in enumerate(table_names, 1):
    print(f"{i}. {table[0]}")

# Ask the user to select a table
table_index = int(input("Enter the number of the table you want to view: ")) - 1

# Get the selected table name
selected_table = table_names[table_index][0]

# Fetch and display the contents of the selected table
cursor.execute(f"SELECT * FROM {selected_table};")
table_contents = cursor.fetchall()

print(f"Contents of the '{selected_table}' table:")
for row in table_contents:
    print(row)

# Close the database connection
conn.close()
