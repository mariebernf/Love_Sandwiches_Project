import gspread
from google.oauth2.service_account import Credentials

# Provide the absolute path to the creds.json file
creds_file_path = 'C:\\Users\\marie\\OneDrive\\Documents\\vscode-projects\\Love_Sandwiches_Project\\creds.json'

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate and authorize
CREDS = Credentials.from_service_account_file(creds_file_path)
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Access the Google Sheet by its name
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# Function to get sales data
def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

# Call the function
get_sales_data()
