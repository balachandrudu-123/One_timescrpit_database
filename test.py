import pandas as pd
import mysql.connector

# Database connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Balu@424",
    "database": "version6",
}

# CSV file path
csv_file_path = r"F:\database\client.csv"

table_name = "client_data"


def insert_data_into_mysql():
    # Connect to MySQL
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    try:
        # Read CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Iterate through rows and insert into MySQL
        for index, row in df.iterrows():
            values = tuple(row)
            placeholders = ", ".join(["%s"] * len(row))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"

            try:
                cursor.execute(query, values)
            except mysql.connector.IntegrityError as e:
                print(f"Skipping duplicate entry: {e}")
                connection.rollback()  # Rollback the transaction for this specific row

        # Commit the changes
        connection.commit()
        return "Data inserted successfully!"

    except Exception as e:
        return f"Error: {e}"

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


result = insert_data_into_mysql()
print(result)
