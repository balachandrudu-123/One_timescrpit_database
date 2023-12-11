import csv
import json
import requests


def send_row_to_api(row, backend_api_url):
    try:
        # Convert row data to JSON string
        json_data = json.dumps(row, indent=2)

        # Send JSON data to the backend API
        headers = {"Content-Type": "application/json"}
        response = requests.post(backend_api_url, data=json_data, headers=headers)

        if response.status_code == 200:
            print(f"Row sent successfully to the API: {row}")
        else:
            print(
                f"Failed to send row. API returned {response.status_code} status code."
            )
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def csv_to_api(csv_file_path, backend_api_url):
    with open(csv_file_path, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Iterate through each row and send to API
        for row in csv_reader:
            send_row_to_api(row, backend_api_url)


def add_user_roles(static_roles, backend_api_url):
    try:
        # Convert static roles data to JSON string
        json_data = json.dumps(static_roles, indent=2)

        # Send JSON data to the backend API
        headers = {"Content-Type": "application/json"}
        response = requests.post(backend_api_url, data=json_data, headers=headers)

        if response.status_code == 200:
            print(f"Static user roles stored successfully: {static_roles}")
        else:
            print(
                f"Failed to store static user roles. API returned {response.status_code} status code."
            )
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


csv_file_path = r"F:\database\medical_conditions.csv"
backend_api_url_add_doctor = "http://localhost:5570/getpatient/medical_conditions/add_medical_condition"
backend_api_url_add_roles = "http://localhost:5570/auth/login/add_user_roles"

# Get user input to decide which function to run
option = input("Enter 1 to run csv_to_api, 2 to run add_user_roles: ")

if option == "1":
    csv_to_api(csv_file_path, backend_api_url_add_doctor)
elif option == "2":
    static_user_roles = {"roles": ["doctor2", "nurse3"]}
    add_user_roles(static_user_roles, backend_api_url_add_roles)
else:
    print("Invalid option. Please enter 1 or 2.")
