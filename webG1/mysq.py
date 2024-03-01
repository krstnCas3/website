import mysql.connector

# Replace these with your MySQL server credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'secret13',
    'database': 'demo',
}

# Establish a connection to the MySQL server
try:
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MySQL server")

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Create a table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS example_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("Table created successfully")

        # Insert data into the table
        insert_data_query = "INSERT INTO example_table (name, age) VALUES (%s, %s)"
        data_to_insert = [("John", 25), ("Jane", 30), ("Bob", 22)]

        cursor.executemany(insert_data_query, data_to_insert)
        connection.commit()
        print("Data inserted successfully")

        # Query data from the table
        select_data_query = "SELECT * FROM example_table"
        cursor.execute(select_data_query)

        # Fetch and print the results
        rows = cursor.fetchall()
        print("Query results:")
        for row in rows:
            print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection in the finally block to ensure cleanup
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
